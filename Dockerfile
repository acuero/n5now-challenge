FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r /app/requirements.txt

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

RUN sed -i 's/\r$//g' /app/start.sh
RUN chmod +x /app/start.sh

RUN sed -i 's/\r$//g' /app/start-demo.sh
RUN chmod +x /app/start-demo.sh

ENTRYPOINT ["bash", "-e", "/app/entrypoint.sh"]
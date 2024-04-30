#!/bin/sh

if [ "$POSTGRES_DB" = "postgres" ]
then
    echo "Esperando por PostgreSQL..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL está listo"
fi

exec "$@"
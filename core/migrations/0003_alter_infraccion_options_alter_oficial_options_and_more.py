# Generated by Django 4.1.13 on 2024-04-26 20:55

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_configuracion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infraccion',
            options={'verbose_name': 'Infracción', 'verbose_name_plural': 'Infracciones'},
        ),
        migrations.AlterModelOptions(
            name='oficial',
            options={'verbose_name': 'Oficial', 'verbose_name_plural': 'Oficiales'},
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='dias_antiguedad_infraccion',
            field=models.PositiveIntegerField(default=90, help_text='Una infracción se considera válida si su antiguedad en días es menor o igual a este valor.', unique=True, verbose_name='Antiguedad válida de una infraccion (dias)'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la creación de un objeto.', verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='nombre',
            field=models.CharField(default='CONFIGURACION_GENERAL', help_text='Configuración General.', max_length=90, unique=True, verbose_name='Configuración'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Campo abierto para añadir alguna descripción u observación.', max_length=255, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Marca de tiempo de la última modificación de un objeto.', verbose_name='Ultima modificación'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la creación de un objeto.', verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='fecha_infraccion',
            field=models.DateTimeField(help_text='Fecha de la infracción', verbose_name='Fecha de la infracción'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Campo abierto para añadir alguna descripción u observación.', max_length=255, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='oficial',
            field=models.ForeignKey(help_text='Oficial que cargó la infracción.', on_delete=django.db.models.deletion.CASCADE, to='core.oficial'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Marca de tiempo de la última modificación de un objeto.', verbose_name='Ultima modificación'),
        ),
        migrations.AlterField(
            model_name='infraccion',
            name='vehiculo',
            field=models.ForeignKey(help_text='Vehículo al que se le carga una infracción.', on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la creación de un objeto.', verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(help_text='Nombre de la marca.', max_length=30, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Campo abierto para añadir alguna descripción u observación.', max_length=255, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Marca de tiempo de la última modificación de un objeto.', verbose_name='Ultima modificación'),
        ),
        migrations.AlterField(
            model_name='oficial',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la creación de un objeto.', verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='oficial',
            name='nombre',
            field=models.CharField(help_text='Nombre del oficial.', max_length=50, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='oficial',
            name='nui',
            field=models.CharField(help_text='Número único identificatorio del oficial.', max_length=10, unique=True, verbose_name='Número único identificatorio'),
        ),
        migrations.AlterField(
            model_name='oficial',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Campo abierto para añadir alguna descripción u observación.', max_length=255, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='oficial',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Marca de tiempo de la última modificación de un objeto.', verbose_name='Ultima modificación'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(help_text='Correo electrónico del propietario.', max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la creación de un objeto.', verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(help_text='Nombre del propietario.', max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Campo abierto para añadir alguna descripción u observación.', max_length=255, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Marca de tiempo de la última modificación de un objeto.', verbose_name='Ultima modificación'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', help_text='Color del vehículo.', image_field=None, max_length=25, samples=None, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la creación de un objeto.', verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.ForeignKey(help_text='Marca del vehículo.', on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='core.marca'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Campo abierto para añadir alguna descripción u observación.', max_length=255, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa_patente',
            field=models.CharField(help_text='Placa de patente del vehículo.', max_length=10, unique=True, verbose_name='Placa patente'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='propietario',
            field=models.ForeignKey(help_text='Propietario del vehículo.', on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='core.persona'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True, help_text='Marca de tiempo de la última modificación de un objeto.', verbose_name='Ultima modificación'),
        ),
    ]

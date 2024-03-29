# Generated by Django 5.0.3 on 2024-03-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionFinanciera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('egresos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pasivos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('historial_crediticio', models.TextField(blank=True, null=True)),
                ('puntuacion_crediticia', models.IntegerField(blank=True, null=True)),
                ('antiguedad_laboral', models.IntegerField()),
                ('tipo_empleo', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(max_length=50)),
                ('numero_dependientes', models.IntegerField(default=0)),
                ('historial_bancario', models.TextField(blank=True, null=True)),
                ('garantias', models.TextField(blank=True, null=True)),
                ('tipo_vivienda', models.CharField(max_length=100)),
                ('educacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'InformacionFinanciera',
                'verbose_name_plural': 'InformacionFinanciera',
                'ordering': ['ingresos'],
            },
        ),
    ]

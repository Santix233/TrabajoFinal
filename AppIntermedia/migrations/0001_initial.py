# Generated by Django 4.1.4 on 2023-01-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Pais', models.CharField(max_length=30)),
                ('Provincia', models.CharField(max_length=30)),
                ('Cuenta', models.IntegerField()),
                ('Sucursal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Identidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Pais', models.CharField(max_length=50)),
                ('Provincia', models.CharField(max_length=50)),
                ('Localidad', models.CharField(max_length=50)),
            ],
        ),
    ]

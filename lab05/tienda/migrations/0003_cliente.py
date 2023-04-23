# Generated by Django 3.2 on 2023-04-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
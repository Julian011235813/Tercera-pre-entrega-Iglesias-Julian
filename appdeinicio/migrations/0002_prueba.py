# Generated by Django 5.0.6 on 2024-06-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdeinicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50)),
                ('dificultad', models.CharField(max_length=50)),
            ],
        ),
    ]

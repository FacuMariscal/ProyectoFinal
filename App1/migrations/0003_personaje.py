# Generated by Django 4.2.5 on 2023-10-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_usuario_delete_fechadecreacion_delete_nickname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fuerza', models.IntegerField()),
                ('velocidad', models.IntegerField()),
                ('resistencia', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
    ]

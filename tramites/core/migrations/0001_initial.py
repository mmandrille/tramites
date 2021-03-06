# Generated by Django 2.0.5 on 2018-05-29 15:08

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('icono', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='archivos/'), upload_to='')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramite',
            name='online',
            field=models.BooleanField(default=True),
        ),
    ]
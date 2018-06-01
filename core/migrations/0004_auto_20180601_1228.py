# Generated by Django 2.0.5 on 2018-06-01 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180529_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='organismo',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tramite',
            name='organismo',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivos', to='core.Guia'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-13 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210313_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='DateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

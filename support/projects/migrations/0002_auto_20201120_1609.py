# Generated by Django 2.1.5 on 2020-11-20 16:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(verbose_name=datetime.datetime(2020, 11, 20, 16, 9, 26, 818267, tzinfo=utc)),
        ),
    ]
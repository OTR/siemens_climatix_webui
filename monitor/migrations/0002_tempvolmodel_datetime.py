# Generated by Django 3.2 on 2021-04-24 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempvolmodel',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 3, 0)),
        ),
    ]

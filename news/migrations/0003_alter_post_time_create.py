# Generated by Django 4.2 on 2023-07-04 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 11, 38, 36, 465229)),
        ),
    ]

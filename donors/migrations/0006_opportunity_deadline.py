# Generated by Django 4.0.3 on 2022-04-08 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0005_rename_detail_opportunity_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

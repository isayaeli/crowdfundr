# Generated by Django 4.1.2 on 2022-11-03 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0029_alter_donation_donated_on_alter_project_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donated_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 3, 16, 43, 57, 55907)),
        ),
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='word_of_support',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 3, 16, 43, 57, 55907)),
        ),
    ]

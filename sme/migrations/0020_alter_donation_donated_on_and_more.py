# Generated by Django 4.0.4 on 2022-06-07 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0019_alter_donation_donated_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donated_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 7, 14, 49, 25, 413080)),
        ),
        migrations.AlterField(
            model_name='word_of_support',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 7, 14, 49, 25, 413546)),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-09 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0026_alter_donation_donated_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donated_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 16, 9, 30, 279363)),
        ),
        migrations.AlterField(
            model_name='word_of_support',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 16, 9, 30, 279854)),
        ),
    ]

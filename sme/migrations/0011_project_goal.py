# Generated by Django 4.0.4 on 2022-05-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0010_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='goal',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0011_project_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.IntegerField(default=0),
        ),
    ]

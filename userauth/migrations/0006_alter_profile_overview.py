# Generated by Django 4.0.4 on 2022-06-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_rename_ngo_overview_profile_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='overview',
            field=models.TextField(blank=True, max_length=320, null=True),
        ),
    ]
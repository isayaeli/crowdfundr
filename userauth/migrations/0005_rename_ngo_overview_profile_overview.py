# Generated by Django 4.0.4 on 2022-06-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_profile_ngo_overview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='ngo_overview',
            new_name='overview',
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_alter_profile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ngo_overview',
            field=models.TextField(blank=True, null=True),
        ),
    ]

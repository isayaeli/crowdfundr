# Generated by Django 4.0.4 on 2022-06-02 16:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sme', '0017_donation_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='word',
        ),
        migrations.AddField(
            model_name='donation',
            name='donated_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 19, 8, 28, 422550)),
        ),
        migrations.CreateModel(
            name='Word_of_support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(null=True)),
                ('added_on', models.DateTimeField(default=datetime.datetime(2022, 6, 2, 19, 8, 28, 423001))),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sme.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
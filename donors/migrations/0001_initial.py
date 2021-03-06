# Generated by Django 4.0.3 on 2022-04-08 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='opps_images')),
                ('detail', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
            },
        ),
    ]

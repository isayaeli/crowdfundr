# Generated by Django 3.2 on 2022-05-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0006_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.FileField(default='brif.png', upload_to='project_image'),
        ),
    ]

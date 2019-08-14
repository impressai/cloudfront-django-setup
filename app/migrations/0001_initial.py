# Generated by Django 2.2.4 on 2019-08-14 07:23

from django.db import migrations, models
import http_project.storage_backends


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=http_project.storage_backends.PrivateMediaStorage(), upload_to='private')),
            ],
        ),
        migrations.CreateModel(
            name='PublicImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=http_project.storage_backends.PublicMediaStorage(), upload_to='public')),
            ],
        ),
    ]

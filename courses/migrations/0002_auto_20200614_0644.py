# Generated by Django 3.0.7 on 2020-06-14 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='slug',
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200616_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

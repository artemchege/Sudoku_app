# Generated by Django 3.1.6 on 2021-02-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210219_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrix',
            name='solved',
            field=models.BooleanField(default=None),
        ),
    ]

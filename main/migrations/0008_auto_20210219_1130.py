# Generated by Django 3.1.6 on 2021-02-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210219_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matrix',
            name='solved',
        ),
        migrations.AddField(
            model_name='matrix',
            name='if_solved',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='matrix',
            name='result',
            field=models.JSONField(default=None),
            preserve_default=False,
        ),
    ]

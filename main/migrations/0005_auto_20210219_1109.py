# Generated by Django 3.1.6 on 2021-02-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210219_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrix',
            name='user',
            field=models.TextField(default=None, max_length=50),
        ),
    ]
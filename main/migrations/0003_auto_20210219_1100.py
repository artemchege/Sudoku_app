# Generated by Django 3.1.6 on 2021-02-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_matrix_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrix',
            name='user',
            field=models.TextField(default=None, max_length=50),
        ),
    ]
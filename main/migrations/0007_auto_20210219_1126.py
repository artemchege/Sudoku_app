# Generated by Django 3.1.6 on 2021-02-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_matrix_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrix',
            name='solved',
            field=models.BooleanField(default=None, null=True),
        ),
    ]

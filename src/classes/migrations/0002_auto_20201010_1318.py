# Generated by Django 2.0 on 2020-10-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(max_length=30),
        ),
    ]

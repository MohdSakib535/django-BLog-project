# Generated by Django 3.2.4 on 2021-10-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Desc',
            field=models.TextField(max_length=2000),
        ),
    ]
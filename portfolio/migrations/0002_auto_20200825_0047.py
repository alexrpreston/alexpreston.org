# Generated by Django 3.0.7 on 2020-08-25 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-24 02:42

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='notes',
            field=markdownx.models.MarkdownxField(default=None),
        ),
    ]

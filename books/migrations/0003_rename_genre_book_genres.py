# Generated by Django 3.2 on 2022-05-03 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='genres',
        ),
    ]
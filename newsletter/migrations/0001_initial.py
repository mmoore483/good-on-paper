# Generated by Django 3.2 on 2022-05-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

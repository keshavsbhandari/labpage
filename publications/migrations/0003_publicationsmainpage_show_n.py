# Generated by Django 3.1.7 on 2021-04-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publicationspage_show_front'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationsmainpage',
            name='show_n',
            field=models.IntegerField(default=2),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_peoplepage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplepage',
            name='display_priority',
            field=models.IntegerField(default=1),
        ),
    ]

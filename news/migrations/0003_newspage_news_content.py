# Generated by Django 3.1.7 on 2021-04-08 16:11

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsmainpage_show_n'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='news_content',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]

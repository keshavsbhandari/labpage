# Generated by Django 3.1.7 on 2021-04-08 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('people', '0002_peoplemainpage_order_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplepage',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]

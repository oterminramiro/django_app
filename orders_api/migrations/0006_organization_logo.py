# Generated by Django 3.0.8 on 2020-07-13 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders_api', '0005_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='static/img/uploads/organization/'),
            preserve_default=False,
        ),
    ]

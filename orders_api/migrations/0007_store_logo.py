# Generated by Django 3.0.8 on 2020-07-13 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders_api', '0006_organization_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='logo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='static/img/uploads/store/'),
            preserve_default=False,
        ),
    ]
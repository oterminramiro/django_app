# Generated by Django 3.0.8 on 2020-07-07 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Organization')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Status')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Status'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Order')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.OrderItemStatus')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Status'),
        ),
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Store'),
        ),
        migrations.CreateModel(
            name='CustomerCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders_api.Customer')),
            ],
        ),
    ]

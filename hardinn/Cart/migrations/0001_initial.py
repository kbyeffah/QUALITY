# Generated by Django 5.1.1 on 2024-11-06 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='ProductImages/')),
                ('quantity', models.IntegerField()),
                ('code', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Cart.product')),
                ('image1', models.ImageField(null=True, upload_to='ExtraProductImage/')),
                ('image2', models.ImageField(null=True, upload_to='ExtraProductImage/')),
                ('image3', models.ImageField(null=True, upload_to='ExtraProductImage/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Cart.product')),
                ('network', models.TextField(default='No Information at the moment', max_length=2000)),
                ('battery', models.TextField(default='No Information at the moment', max_length=2000)),
                ('memory', models.TextField(default='No Information at the moment', max_length=2000)),
                ('processor', models.TextField(default='No Information at the moment', max_length=2000)),
                ('brand', models.TextField(default='No Information at the moment', max_length=2000)),
            ],
        ),
    ]

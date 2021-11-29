# Generated by Django 3.1.2 on 2021-11-25 23:29

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20211122_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, storage=products.storages.ProtectedStorage, upload_to='protected/products/'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-11-22 19:37

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(blank=True, null=True, storage=products.storages.ProtectedStorage, upload_to='products/'),
        ),
    ]

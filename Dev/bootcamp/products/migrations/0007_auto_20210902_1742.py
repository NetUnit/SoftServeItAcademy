# Generated by Django 3.1.2 on 2021-09-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_manufacturers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
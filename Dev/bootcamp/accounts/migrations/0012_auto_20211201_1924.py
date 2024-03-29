# Generated by Django 3.1.2 on 2021-12-01 17:24

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20211101_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/accounts/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='media',
            field=models.FileField(blank=True, null=True, storage=products.storages.ProtectedStorage, upload_to='protected/accounts/'),
        ),
    ]

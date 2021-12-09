# Generated by Django 3.1.2 on 2021-11-25 23:29

from django.db import migrations, models
import products.storages


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0004_auto_20210708_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/manufacturers/'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='media',
            field=models.FileField(blank=True, null=True, storage=products.storages.ProtectedStorage, upload_to='protected/manufacturers/'),
        ),
    ]
# Generated by Django 3.1.2 on 2021-07-08 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0003_auto_20210621_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ('id',)},
        ),
    ]
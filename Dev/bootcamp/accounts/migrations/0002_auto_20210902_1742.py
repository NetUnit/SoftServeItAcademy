# Generated by Django 3.1.2 on 2021-09-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('nickname', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]

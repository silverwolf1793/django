# Generated by Django 3.0.7 on 2020-06-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200615_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Tag',
        ),
        migrations.AddField(
            model_name='product',
            name='Tag',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200615_1242'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumer',
            new_name='Custumer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Costumer',
            new_name='custumer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Product',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
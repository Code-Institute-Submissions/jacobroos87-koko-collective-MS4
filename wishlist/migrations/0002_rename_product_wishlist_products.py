# Generated by Django 3.2.4 on 2021-07-28 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='product',
            new_name='products',
        ),
    ]

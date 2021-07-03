# Generated by Django 3.2.4 on 2021-07-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_featured',
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
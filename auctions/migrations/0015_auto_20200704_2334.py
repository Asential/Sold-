# Generated by Django 3.0.7 on 2020-07-04 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='wishlist',
            new_name='item',
        ),
    ]

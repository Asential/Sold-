# Generated by Django 3.0.7 on 2020-07-04 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.CharField(default=False, max_length=64),
            preserve_default=False,
        ),
    ]
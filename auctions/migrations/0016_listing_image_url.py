# Generated by Django 3.0.7 on 2020-07-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20200704_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]

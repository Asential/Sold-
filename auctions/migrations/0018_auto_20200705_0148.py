# Generated by Django 3.0.7 on 2020-07-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20200705_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(blank=True, default=False, max_length=300),
            preserve_default=False,
        ),
    ]

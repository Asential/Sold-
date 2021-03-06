# Generated by Django 3.0.7 on 2020-07-03 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200704_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('category', models.CharField(choices=[('None', 'None'), ('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home')], default='None', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='item',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='placer',
            field=models.CharField(max_length=64, null=True),
        ),
    ]

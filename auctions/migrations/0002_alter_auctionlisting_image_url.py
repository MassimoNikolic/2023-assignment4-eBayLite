# Generated by Django 4.0.3 on 2023-10-30 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image_url',
            field=models.URLField(default='https://www.bahmansport.com/media/com_store/images/empty.png'),
        ),
    ]

# Generated by Django 2.2.12 on 2020-11-06 10:12

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('first_price_auction', '0002_auto_20201030_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bid',
            field=otree.db.models.CurrencyField(null=True, verbose_name='Please enter your bid.'),
        ),
    ]
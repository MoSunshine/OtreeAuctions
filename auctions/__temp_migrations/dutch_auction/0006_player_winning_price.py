# Generated by Django 2.2.12 on 2020-10-16 17:30

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('dutch_auction', '0005_auto_20201016_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='winning_price',
            field=otree.db.models.CurrencyField(null=True),
        ),
    ]

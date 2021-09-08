# Generated by Django 2.2.12 on 2020-10-16 13:08

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('dutch_auction', '0002_auto_20201016_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_winner',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
    ]
# Generated by Django 2.2.3 on 2019-09-23 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0009_regfm_votecast_voteresult'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VoteCast',
        ),
    ]

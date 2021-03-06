# Generated by Django 2.2.3 on 2019-09-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0003_delete_voteresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=19, unique=True)),
                ('party', models.CharField(choices=[('apc', 'APC'), ('apga', 'APGA'), ('pdc', 'PDC'), ('pdm', 'PDM'), ('pdp', 'PDP'), ('sdc', 'SDC')], default='apc', max_length=50)),
                ('date_voted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'voteresult',
                'ordering': ['-party'],
            },
        ),
    ]

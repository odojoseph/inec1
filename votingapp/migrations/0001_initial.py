# Generated by Django 2.2.3 on 2019-09-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegFm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField(default='0000-01-31')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'registrationform',
                'ordering': ['-last_name'],
            },
        ),
    ]
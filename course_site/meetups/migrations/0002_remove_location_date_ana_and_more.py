# Generated by Django 4.0 on 2021-12-24 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='date_ana',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='date_auto_now',
        ),
    ]

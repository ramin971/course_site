# Generated by Django 4.0 on 2021-12-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]

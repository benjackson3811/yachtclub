# Generated by Django 3.2.22 on 2023-10-14 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='trip_categories',
        ),
    ]
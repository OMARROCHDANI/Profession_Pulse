# Generated by Django 4.2.2 on 2023-09-11 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_savedjobs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SavedJobs',
        ),
    ]

# Generated by Django 2.2 on 2019-05-09 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talkbot', '0013_auto_20190509_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='date',
            new_name='date_created',
        ),
    ]

# Generated by Django 2.2 on 2019-05-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talkbot', '0007_auto_20190509_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_update',
            name='desciption',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
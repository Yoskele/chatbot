# Generated by Django 2.2 on 2019-04-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talkbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatt',
            name='message',
            field=models.TextField(max_length=400),
        ),
    ]

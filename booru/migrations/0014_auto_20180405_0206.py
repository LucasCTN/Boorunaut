# Generated by Django 2.0 on 2018-04-05 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booru', '0013_auto_20180405_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='account',
            new_name='author',
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-19 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_account_followers_alter_account_subscriptions_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='Accounts',
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-21 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_likes_twit_alter_twits_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twits',
            name='like',
        ),
    ]

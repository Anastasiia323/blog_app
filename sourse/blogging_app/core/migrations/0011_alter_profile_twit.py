# Generated by Django 4.2.4 on 2023-08-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_countries_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twit',
            field=models.ManyToManyField(db_table='profile_twits', related_name='profile', to='core.twits'),
        ),
    ]

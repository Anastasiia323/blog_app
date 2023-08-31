# Generated by Django 4.2.4 on 2023-08-12 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_twits_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

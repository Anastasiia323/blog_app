# Generated by Django 4.2.4 on 2023-08-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_emailconfirmationcode_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]

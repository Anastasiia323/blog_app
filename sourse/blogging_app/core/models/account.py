from django.db import models
from django.contrib.auth import get_user_model


class Account(models.Model):
    file = models.ImageField(upload_to='profile/photo/', null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    following = models.ManyToManyField(
        to=get_user_model(),
        related_name='fallowing',
        blank=True
    )
    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True
    )
    country = models.ForeignKey(
        to='Countries',
        on_delete=models.CASCADE,
        related_name='account'
    )
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Accounts'


class Profile(models.Model):
    class Meta:
        db_table = 'Profile'


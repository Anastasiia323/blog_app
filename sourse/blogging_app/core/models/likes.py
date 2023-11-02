from django.db import models
from django.contrib.auth import get_user_model
from .twits import Twits
from .account import Account


class Likes(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='likes',
        on_delete=models.CASCADE,
        blank=True
    )
    twit = models.ForeignKey(
        to='Twits',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Likes'

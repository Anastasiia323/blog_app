from django.db import models
from .twits import Twits
from django.contrib.auth import get_user_model


class Comments(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments'

    )
    twit = models.ForeignKey(
        to='Twits',
        on_delete=models.CASCADE,
        related_name='comments'

    )
    body = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Comments'




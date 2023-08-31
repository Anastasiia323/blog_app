from django.db import models
from django.contrib.auth import get_user_model
from .tags import Tags


class Twits(models.Model):
    name = models.CharField(max_length=256)
    tags = models.ManyToManyField(
        to='Tags',
        related_name='twits',
        db_table='twits_tags'
    )
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='twit',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Twits'

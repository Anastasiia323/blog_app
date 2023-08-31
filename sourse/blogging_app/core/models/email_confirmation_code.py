from django.db import models
from django.contrib.auth import get_user_model


class EmailConfirmationCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='user'
    )
    expiration = models.PositiveIntegerField()

    class Meta:
        db_table = 'Email_Confirmation_Code'


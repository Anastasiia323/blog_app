from __future__ import annotations
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
import uuid
import time
import random
from ..dto.create_user import CreateUserDTO
from ..exceptions import (
    ConfirmationCodeExpired,
    ConfirmationCodeDoesNotExist
)
from ...models import EmailConfirmationCode


def add_user(data: CreateUserDTO) -> None:
    user_model = get_user_model()
    created_user = user_model.objects.create_user(username=data.username,
                                                  email=data.email,
                                                  password=data.password,
                                                  is_active=False)

    confirmation_code = str(uuid.uuid4())
    code_expiration_time = int(time.time()) + settings.CONFIRMATION_CODE_LIFETIME
    confirmation_url = settings.SERVER_HOST + reverse('confirm') + f'?code={confirmation_code}'
    EmailConfirmationCode.objects.create(
        user=created_user,
        expiration=code_expiration_time,
        code=confirmation_code
    )
    send_mail(
        subject='Confirm your email',
        message=f"Please confirm your email by clicking the link below:\n\n{confirmation_url}",
        from_email=settings.EMAIL_FROM,
        recipient_list=[data.email]
    )


def confirmation_user(confirmation_code: str) -> None:
    try:
        data = EmailConfirmationCode.objects.get(code=confirmation_code)

    except EmailConfirmationCode.DoesNotExist:
        raise ConfirmationCodeDoesNotExist('Confirmation Code Does Not Exist')

    if time.time() > data.expiration:
        raise ConfirmationCodeExpired

    user = data.user
    user.is_active = True
    user.save()

    data.delete()

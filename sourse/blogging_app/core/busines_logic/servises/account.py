from __future__ import annotations
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from ..dto.account import (
    AddAccountDTO,
    ChangeEmailDTO,
    AccountEditDTO,
    ChangePhotoDTO
)
from ...models import Account, Countries, EmailConfirmationCode
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid
import time


def create_account(data: AddAccountDTO, user) -> None:
    data.username = get_user_model().objects.get(username=user)
    file_extension = data.file.name.split(".")[-1]
    file_name = str(uuid.uuid4()) + "." + file_extension
    data.file.name = file_name
    try:
        data.country = Countries.objects.get(name=data.country)
    except Countries.DoesNotExist:
        data.country = Countries.objects.create(name=data.country)

    Account.objects.create(file=data.file, user=data.username, name=data.first_name,
                           surname=data.last_name, description=data.description, country=data.country)


def get_account(request) -> Account:
    account = Account.objects.filter(user=request.user)
    return account


def edit_account(data: AccountEditDTO, user: AbstractBaseUser) -> None:
    account = Account.objects.get(user=user)
    account.name = data.first_name
    account.surname = data.last_name
    account.country.name = data.country
    account.description = data.description

    account.save()


def edit_email(user: AbstractBaseUser, data: ChangeEmailDTO):
    account = Account.objects.get(user=user)
    account.user.email = data.email
    account.save()
    user = get_user_model().objects.get(username=user)
    confirmation_code = str(uuid.uuid4())
    code_expiration_time = int(time.time()) + settings.CONFIRMATION_CODE_LIFETIME
    confirmation_url = settings.SERVER_HOST + reverse('confirm-email') + f'?code={confirmation_code}'
    EmailConfirmationCode.objects.create(user=user,
                                         expiration=code_expiration_time,
                                         code=confirmation_code)
    send_mail(
        subject='Confirm your email',
        message=f"Please confirm your email by clicking the link below:\n\n{confirmation_url}",
        from_email=settings.EMAIL_FROM,
        recipient_list=[data.email]
    )


def get_account_data(user: AbstractBaseUser) -> Account:
    account = Account.objects.get(user=user)
    return account


def change_photo(data: ChangePhotoDTO, user: AbstractBaseUser) -> None:
    account = Account.objects.get(user=user)
    file_extension = data.file.name.split(".")[-1]
    file_name = str(uuid.uuid4()) + "." + file_extension
    data.file.name = file_name
    account.file = data.file

    account.save()

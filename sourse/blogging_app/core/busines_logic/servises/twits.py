from __future__ import annotations
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.contrib.auth.models import AbstractBaseUser
from ..dto.twits import AddTwitDTO, EditTwitDTO
from ...models import Twits


def twit_list(request) -> [Twits]:
    twits = Twits.objects.filter(user=request.user).order_by('-name')
    return list(twits)


def send_twit(data: AddTwitDTO, user: AbstractBaseUser) -> None:
    data.user = get_user_model().objects.get(username=user)
    Twits.objects.create(name=data.name, user=data.user)


def twit_by_id(twit_id: int):
    twit = Twits.objects.select_related('user').get(pk=twit_id)
    return twit


def delete_twit(twit_id: int):
    twit = Twits.objects.select_related('user').get(pk=twit_id)
    twit.delete()


def edit_twit(twit_id: int, data: EditTwitDTO):
    twit = Twits.objects.select_related('user').get(pk=twit_id)
    twit.name = data.name
    twit.save()





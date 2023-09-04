from __future__ import annotations
from django.contrib.auth import get_user_model
from django.db import transaction
from django.contrib.auth.models import AbstractBaseUser
from ..dto.twits import AddTwitDTO, EditTwitDTO, SearchTwitDTO
from ...models import Twits, Tags


def twit_list(request) -> tuple[[Twits], [Tags]]:
    twits = Twits.objects.filter(user=request.user).order_by('-name')
    for twit in twits:
        tags = twit.tags.all
        return twits, tags


def send_twit(data: AddTwitDTO, user: AbstractBaseUser) -> None:
    data.user = get_user_model().objects.get(username=user)
    tags = data.tags.split(',')
    tags_list: list[Tag] = []
    for tag in tags:
        tag = tag.lower()
        try:
            tag_from_db = Tags.objects.get(name=tag)
        except Tags.DoesNotExist:
            tag_from_db = Tags.objects.create(name=tag)

        tags_list.append(tag_from_db)

    twit = Twits.objects.create(name=data.name, user=data.user)
    twit.tags.set(tags_list)


def twit_by_id(twit_id: int) -> tuple[[Twits], [Tags]]:
    twit = Twits.objects.select_related('user').prefetch_related('tags').get(pk=twit_id)
    tags = twit.tags.all()
    return twit, tags


def get_twit(twit_id: int) -> Twits:
    twit = Twits.objects.select_related('user').get(pk=twit_id)
    return twit


def delete_twit(twit_id: int):
    twit = Twits.objects.select_related('user').get(pk=twit_id)
    twit.delete()


def edit_twit(twit_id: int, data: EditTwitDTO):
    twit = Twits.objects.select_related('user').get(pk=twit_id)
    twit.name = data.name
    twit.save()


def get_twits_by_tag(tag_id: int) -> tuple[[Twits], [Tags]]:
    twits = Twits.objects.filter(tags__id=tag_id)
    for twit in twits:
        tags = twit.tags.all
        return twits, tags


def search_twits(search_by_tag: SearchTwitDTO) -> tuple[[Twits], [Tags]]:
    twits = Twits.objects.select_related('user').prefetch_related('tags')
    if search_by_tag.tag:
        twits = Twits.objects.filter(tags__name=search_by_tag.tag)
    for twit in twits:
        tags = twit.tags.all()
        return twits, tags

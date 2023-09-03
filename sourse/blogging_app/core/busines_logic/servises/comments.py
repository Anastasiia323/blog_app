from __future__ import annotations
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from ...models import Twits
from ..dto.comments import CreateCommentDTO
from ...models.comments import Comments
from .twits import get_twit


def create_comment(
        data: CreateCommentDTO,
        user: AbstractBaseUser,
        twit_id: int
):
    data.user = get_user_model().objects.get(username=user)
    data.twit_id = get_twit(twit_id=twit_id)
    Comments.objects.create(user=data.user,
                            twit=data.twit_id,
                            body=data.name)


def comments_list(twit_id: int) -> [Comments]:
    comments = Comments.objects.filter(twit_id=twit_id)
    return list(comments)


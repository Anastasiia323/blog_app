from __future__ import annotations
from ...models import Likes
from ...models import Twits
from ...models import Account


def add_likes(twit_id: int, user):
    twit = Twits.objects.get(pk=twit_id)
    username = Account.objects.get(user=user).user.id
    like = Likes.objects.filter(user=username, twit_id=twit_id)
    if not like:
        Likes.objects.create(twit_id=twit_id, user_id=username)
        twit.like += 1
        twit.save()
    else:
        like.delete()
        twit.like -= 1
        twit.save()













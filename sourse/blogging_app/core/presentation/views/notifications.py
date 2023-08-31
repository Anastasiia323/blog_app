from __future__ import annotations
from django.shortcuts import render, redirect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest


def notifications_controller(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Тут служебные сообщение: кто-то подписался, кто-то лайкнул")
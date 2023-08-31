from __future__ import annotations
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ..convert_to_dto import convert_to_dto


@require_http_methods(request_method_list='GET')
def logout_controller(request: HttpRequest) -> HttpResponse:
    logout(request=request)
    return redirect(to='home')

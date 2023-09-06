from __future__ import annotations
from django.shortcuts import render, redirect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ...busines_logic.servises.account import show_all_accounts


@require_http_methods(request_method_list='GET')
def home_controller(request: HttpRequest) -> HttpResponse:
    accounts = show_all_accounts()
    context = {'accounts': accounts}
    return render(request=request, template_name='home.html', context=context)





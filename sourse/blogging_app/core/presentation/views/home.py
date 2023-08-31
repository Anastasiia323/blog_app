from __future__ import annotations
from django.shortcuts import render, redirect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest


@require_http_methods(request_method_list=['GET', 'POST'])
def home_controller(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')



from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import authenticate
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest
from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ...busines_logic.dto.login import LoginUserDTO
from ..forms.login import LoginUserForm
from ...busines_logic.servises.login import authenticate_user
from ..convert_to_dto import convert_to_dto


@require_http_methods(request_method_list=['GET', 'POST'])
def login_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = LoginUserForm()
        context = {'form': form}
        return render(request=request, template_name='login.html', context=context)
    else:
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(LoginUserDTO, form.cleaned_data)
            try:
                user = authenticate_user(data=data)
            except InvalidAuthenticateData:
                return HttpResponseBadRequest('Invalid username or password. Please, try again')

            login(request=request, user=user)
            return redirect(to='home')
        else:
            context = {'form': form}
            return render(request=request, template_name='login.html', context=context)

from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ..forms.create_user import RegistrationForm
from ...busines_logic.dto.create_user import CreateUserDTO
from ...busines_logic.servises.create_user import add_user, confirmation_user
from ..convert_to_dto import convert_to_dto


@require_http_methods(request_method_list=['GET', 'POST'])
def registrate_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = RegistrationForm()
        context = {'form': form}
        return render(request=request, template_name='sign_up.html', context=context)
    else:
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(CreateUserDTO, form.cleaned_data)
            add_user(data=data)

    return HttpResponseRedirect(redirect_to=reverse("message"))


def email_notification_controller(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='message_after_registration.html')


@require_http_methods(request_method_list=['GET'])
def registration_confirm_controller(request: HttpRequest) -> HttpResponse:
    conformation_code = request.GET['code']
    try:
        confirmation_user(confirmation_code=conformation_code)
    except ConfirmationCodeDoesNotExist:
        return HttpResponseBadRequest('Invalid Confirmation Code')
    except ConfirmationCodeExpired:
        return HttpResponseBadRequest('Confirmation Code Is Expired')

    return redirect(to='login')






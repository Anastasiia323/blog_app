from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from ...busines_logic.exceptions import ConfirmationCodeExpired, ConfirmationCodeDoesNotExist
from ...busines_logic.servises.create_user import confirmation_user

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ...busines_logic.dto.account import (
    AddAccountDTO,
    ChangeEmailDTO,
    AccountEditDTO,
    ChangePhotoDTO
)

from ..forms.account import CreateProfile, EditProfile, ChangeEmail, ChangePhoto
from ..forms.twits import AddTwitForm
from ...busines_logic.servises.account import (
    create_account,
    edit_account,
    edit_email,
    get_account,
    get_account_data,
    change_photo,
    get_account_by_id,
    following,
    follow_unfollow
)
from ...busines_logic.servises.twits import (
    send_twit,
    twit_list,
    twit_by_id
)

from ..convert_to_dto import convert_to_dto


@require_http_methods(request_method_list=['GET'])
def account_controller(request: HttpRequest) -> HttpResponse:
    accounts = get_account(request=request)
    form = AddTwitForm()
    twits = twit_list(request=request)
    context = {'accounts': accounts, 'form': form, 'twits': twits}
    return render(request=request, template_name='account.html', context=context)


@require_http_methods(request_method_list=['GET', 'POST'])
def account_add_controller(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CreateProfile()
        context = {'form': form}
        return render(request=request, template_name='create_account.html',
                      context=context)
    elif request.method == "POST":
        form = CreateProfile(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = convert_to_dto(AddAccountDTO, form.cleaned_data)
            create_account(data=data, user=request.user)

    return HttpResponseRedirect(redirect_to=reverse('account'))


@require_http_methods(request_method_list=['GET', 'POST'])
def account_edit_controller(request: HttpRequest):
    if request.method == 'GET':
        account = get_account_data(user=request.user)
        data = {'file': account.file,
                'first_name': account.name,
                'last_name': account.surname,
                'country': account.country.name,
                'description': account.description
                }
        form = EditProfile(data=data)
        accounts = get_account(request=request)
        context = {'form': form, 'accounts': accounts}
        return render(request=request, template_name='edit_account.html', context=context)
    else:
        form = EditProfile(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(AccountEditDTO, form.cleaned_data)
            edit_account(user=request.user, data=data)
    return HttpResponseRedirect(redirect_to=reverse('account'))


@require_http_methods(request_method_list=['GET', 'POST'])
def change_email_controller(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        account = get_account_data(user=request.user)
        data = {'email': account.user.email}
        form = ChangeEmail(data=data)
        context = {'form': form}
        return render(request=request, context=context, template_name='change_email.html')
    else:
        form = ChangeEmail(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(ChangeEmailDTO, form.cleaned_data)
            edit_email(user=request.user, data=data)

    return HttpResponseRedirect(redirect_to=reverse('message'))


@require_http_methods(request_method_list=['GET'])
def change_email_confirm_controller(request: HttpRequest) -> HttpResponse:
    conformation_code = request.GET['code']
    try:
        confirmation_user(confirmation_code=conformation_code)
    except ConfirmationCodeDoesNotExist:
        return HttpResponseBadRequest('Invalid Confirmation Code')
    except ConfirmationCodeExpired:
        return HttpResponseBadRequest('Confirmation Code Is Expired')

    return redirect(to='account')


@require_http_methods(request_method_list=['GET', 'POST'])
def change_photo_controller(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = ChangePhoto()
        context = {'form': form}
        return render(request=request, template_name='change_photo.html', context=context)
    else:
        form = ChangePhoto(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = convert_to_dto(ChangePhotoDTO, form.cleaned_data)
            change_photo(data=data, user=request.user)

    return redirect(to='account')


@require_http_methods(request_method_list=['GET'])
def get_account_by_id_controller(request: HttpRequest, account_id: int) -> HttpResponse:
    account = get_account_by_id(account_id=account_id)
    followings = following(user=request.user)
    if account.user in followings:
        follow = True
    else:
        follow = False

    context = {'account': account, 'follow': follow}
    return render(request=request, context=context, template_name='get_account_by_id.html')


@require_http_methods(request_method_list=['GET'])
def follow_unfollow_controller(request: HttpRequest, account_id: int) -> HttpResponse:
    follow_unfollow(account_id=account_id, user=request.user)
    return redirect(to='account')


from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ...busines_logic.dto.twits import AddTwitDTO, EditTwitDTO, SearchTwitDTO
from ...busines_logic.servises.twits import (
    send_twit,
    twit_list,
    twit_by_id,
    delete_twit,
    edit_twit,
    get_twit,
    get_twits_by_tag,
    search_twits
)
from ..forms.twits import AddTwitForm, EditTwitForm, SearchTwit
from ..convert_to_dto import convert_to_dto
from ...busines_logic.servises.comments import comments_list


@require_http_methods(request_method_list=['GET', 'POST'])
def add_twit(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = AddTwitForm()
        context = {'form': form}
        return render(request=request, template_name='add_twit.html', context=context)
    else:
        form = AddTwitForm(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(AddTwitDTO, form.cleaned_data)
            send_twit(data=data, user=request.user)

    return HttpResponseRedirect(redirect_to=reverse('account'))


@require_http_methods(request_method_list=['GET'])
def tags_controller(request: HttpRequest) -> HttpResponse:
    form = SearchTwit(request.GET)
    if form.is_valid():
        search_twits_by_tag = convert_to_dto(SearchTwitDTO, form.cleaned_data)
        twits, tags = search_twits(search_by_tag=search_twits_by_tag)
        form = SearchTwit()
        context = {'form': form, 'twits': twits, 'tags': tags}
        return render(request=request, template_name='tags.html', context=context)
    else:
        context = {'form': form}
        return render(request=request, template_name='tags.html', context=context)


@require_http_methods(request_method_list=['GET'])
def get_twit_controller(request: HttpRequest, twit_id: int) -> HttpResponse:
    twit, tags = twit_by_id(twit_id=twit_id)
    comments = comments_list(twit_id=twit_id)
    context = {'twit': twit, 'comments': comments, 'tags': tags}
    return render(request=request, context=context, template_name='twit_by_id.html')


@require_http_methods(request_method_list=['GET'])
def delete_twit_controller(request: HttpRequest, twit_id: int) -> HttpResponse:
    delete_twit(twit_id=twit_id)
    return redirect('account')


@require_http_methods(request_method_list=['GET', 'POST'])
def edit_twit_controller(request: HttpRequest, twit_id: int) -> HttpResponse:
    if request.method == 'GET':
        twit = get_twit(twit_id=twit_id)
        data = {
            'name': twit.name
            }
        form = EditTwitForm(data)
        context = {'form': form, 'twit_id': twit_id}
        return render(request=request, template_name='edit_twit.html', context=context)
    else:
        form = EditTwitForm(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(EditTwitDTO, form.cleaned_data)
            edit_twit(data=data, twit_id=twit_id)
    return redirect(to='account')


@require_http_methods(request_method_list=['GET'])
def get_posts_by_tag_controller(request: HttpRequest, tag_id: int) -> HttpResponse:
    twits, tags = get_twits_by_tag(tag_id=tag_id)
    context = {'twits': twits, 'tags': tags}
    return render(request=request, template_name='twits_by_tags.html', context=context)




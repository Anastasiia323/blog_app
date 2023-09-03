from __future__ import annotations
from django.shortcuts import render, redirect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from ..forms.comments import AddCommentForm
from .twits import twit_by_id
from ...busines_logic.dto.comments import CreateCommentDTO
from ...busines_logic.servises.comments import create_comment
from ..convert_to_dto import convert_to_dto


@require_http_methods(request_method_list=['GET', 'POST'])
def create_comment_controller(request: HttpRequest, twit_id: int):
    if request.method == 'GET':
        form = AddCommentForm()
        twit, tags = twit_by_id(twit_id=twit_id)
        context = {'form': form, 'twit_id': twit_id, 'twit': twit, 'tags': tags}
        return render(request=request, template_name='comments.html', context=context)

    else:
        form = AddCommentForm(data=request.POST)
        if form.is_valid():
            data = convert_to_dto(CreateCommentDTO, form.cleaned_data)
            create_comment(data=data, user=request.user, twit_id=twit_id)
    return redirect(to='account')


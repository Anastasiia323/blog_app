from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpRequest

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from ...busines_logic.servises.like import add_likes


@require_http_methods(request_method_list=['GET'])
def like_twit_controller(request: HttpRequest, twit_id: int) -> HttpResponse:
    add_likes(twit_id=twit_id, user=request.user)
    return redirect('account')









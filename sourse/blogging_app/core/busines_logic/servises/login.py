from __future__ import annotations
from django.contrib.auth import (
    get_user_model,
    authenticate
)
from ..dto.login import LoginUserDTO
from ..exceptions import InvalidAuthenticateData


def authenticate_user(data: LoginUserDTO) -> User:
    user = authenticate(username=data.username, password=data.password)
    if user is not None:
        return user

    else:
        raise InvalidAuthenticateData

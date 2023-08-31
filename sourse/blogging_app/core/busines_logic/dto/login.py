from dataclasses import dataclass


@dataclass
class LoginUserDTO:
    username: str
    password: str

from dataclasses import dataclass
from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class AddAccountDTO:
    file: InMemoryUploadedFile
    first_name: str | None
    last_name: str | None
    country: str
    description: str


@dataclass
class AccountEditDTO:
    first_name: str | None
    last_name: str | None
    country: str | None
    description: str | None


@dataclass
class ChangeEmailDTO:
    email: str


@dataclass
class ChangePhotoDTO:
    file: InMemoryUploadedFile


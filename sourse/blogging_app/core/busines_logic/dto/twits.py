from dataclasses import dataclass


@dataclass
class AddTwitDTO:
    name: str
    tags: str


@dataclass
class EditTwitDTO:
    name: str


@dataclass
class SearchTwitDTO:
    tag: str




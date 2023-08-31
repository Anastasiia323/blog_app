from ..busines_logic.exceptions import ValidationError


class ValidateFileExtension:
    def __init__(self, available_extensions):
        self._available_extensions = available_extensions

    def __call__(self, value):
        file_extensions = value.name.split('.')[-1]
        if file_extensions not in self._available_extensions:
            raise ValidationError(f"Available extensions: {self._available_extensions}")


class ValidateFileSize:
    def __init__(self, max_size):
        self._max_size = max_size

    def __call__(self, value):
        if value.size > self._max_size:
            max_size_in_mb = (self._max_size / 1_000_000)
            raise ValidationError(f"Max size is {max_size_in_mb} MB")


class ValidatePasswordLength:
    def __init__(self, length):
        self._length = length

    def __call__(self, value):
        if len(value) not in self._length:
            raise ValidationError('Password length must be from 8 to 15 symbols')


def validate_swear_words_in_user_name(value: str):
    if 'fuck' in value:
        raise ValidationError('Username contains swear words')


def validate_first_letter_in_password(value: str):
    if value[0] != value[0].upper():
        raise ValidationError('Password must start with capital letter')










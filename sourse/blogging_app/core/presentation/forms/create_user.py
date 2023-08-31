from django import forms
from ..validators import (
    ValidatePasswordLength,
    validate_swear_words_in_user_name,
    validate_first_letter_in_password
)


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput,
        required=True,
        max_length=30,
        validators=[validate_swear_words_in_user_name]
    )
    birthday = forms.CharField(
        label='Birthday',
        widget=forms.DateInput,
        required=True
    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput,
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        validators=[ValidatePasswordLength(length=range(8, 16)),
                    validate_first_letter_in_password]
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput,
        required=True,
        validators=[ValidatePasswordLength(length=range(8, 16)),
                    validate_first_letter_in_password]
    )

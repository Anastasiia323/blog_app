from django import forms
from ...presentation.validators import ValidateFileSize, ValidateFileExtension
from ...models import Account


class CreateProfile(forms.Form):
    file = forms.ImageField(
        label='Add Photo',
        validators=[ValidateFileExtension(['png', 'jpg', 'jpeg']),
                    ValidateFileSize(max_size=30_000_000)],
        required=False
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=30,
        required=True
    )
    last_name = forms.CharField(
        label='Last name',
        max_length=30,
        required=False
    )
    country = forms.CharField(
        label='Country',
        required=False
    )
    description = forms.CharField(
        label='About You',
        max_length=75,
        widget=forms.Textarea,
        required=False)


class EditProfile(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=30,
        required=False
    )
    last_name = forms.CharField(
        label='Last name',
        max_length=30,
        required=False
    )
    country = forms.CharField(
        label='Country',
        required=False
    )
    description = forms.CharField(
        label='About You',
        max_length=75,
        widget=forms.Textarea,
        required=False)


class ChangeEmail(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput, required=True)


class ChangePhoto(forms.Form):
    file = forms.ImageField(label='Change Photo',
                            validators=[ValidateFileExtension(['png', 'jpg', 'jpeg']),
                                        ValidateFileSize(max_size=30_000_000)])

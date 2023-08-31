from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=30,
        required=True
    )
    password = forms.CharField(
        label='Password',
        max_length=30,
        required=True,
        widget=forms.PasswordInput
    )




from django import forms


class AddTwitForm(forms.Form):
    name = forms.CharField(
        label='Twit',
        widget=forms.Textarea,
        max_length=400,
        initial='Text something!'
    )


class EditTwitForm(forms.Form):
    name = forms.CharField(
        label='Twit',
        widget=forms.Textarea,
        max_length=400
    )

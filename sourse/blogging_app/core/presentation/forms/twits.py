from django import forms


class AddTwitForm(forms.Form):
    name = forms.CharField(
        label='Twit',
        widget=forms.Textarea,
        max_length=400,
        initial='Text something!'
    )
    tags = forms.CharField(
        label='Tags',
        widget=forms.Textarea
    )


class EditTwitForm(forms.Form):
    name = forms.CharField(
        label='Twit',
        widget=forms.Textarea,
        max_length=400
    )

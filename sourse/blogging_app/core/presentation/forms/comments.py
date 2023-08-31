from django import forms
from ...models.comments import Comments


class AddCommentForm(forms.Form):
    name = forms.CharField(label='Twit',
                           widget=forms.Textarea,
                           max_length=256,
                           initial='Post your reply!')


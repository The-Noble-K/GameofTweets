from django import forms
from django.utils.html import strip_tags
from gotweet.models import Gotweet

class GotweetForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Gotweet', 'class': 'form-control'}))
    location = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Location', 'class': 'form-control'}))

    class Meta:
        model = Gotweet
        exclude = ('user',)


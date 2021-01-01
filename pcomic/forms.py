from django import forms
from . models import Post

class PostSearchForm(forms.Form):
    q = forms.CharField()
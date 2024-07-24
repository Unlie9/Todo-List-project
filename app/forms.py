from django import forms

from app.models import Tag


class TagForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['name']


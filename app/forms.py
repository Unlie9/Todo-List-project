from django import forms

from app.models import Tag, Task


class TagForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['name']


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'datetime-local'}
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = ['content', 'tags', 'deadline']


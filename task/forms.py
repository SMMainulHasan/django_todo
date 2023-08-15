from django import forms

from task.models import TaskStoreModel


class TaskStoreForm(forms.ModelForm):
    task = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'autofocus': 'autofocus'}))
    detail = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = TaskStoreModel
        fields = {'detail', 'task'}

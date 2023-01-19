from django import forms
from .models import User, Item


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

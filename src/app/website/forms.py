from django import forms
from .models import Item


class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # add "device_mac" if you want it editable
        fields = ["name", "stock", "max_stock", "row", "level", "box"]
        # Or use: exclude = ["created_at"]
        # widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}

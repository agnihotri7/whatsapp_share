"""
"""
from PIL import Image
from django import forms
from models import Item, Purchase


class ItemCreateForm(forms.ModelForm):
    """
    Modal form for Question Create
    """

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'image', 'price', 'inventory']


class OrderCreateForm(forms.ModelForm):
    """
    Modal form for Question Create
    """

    class Meta:
        model = Purchase
        fields = ['id', 'item', 'buyer',]

from django.forms import ModelForm
from django import forms
from main.models import Shop

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["name", "description", "category", "size", "price", "thumbnail", "is_featured"]

class BolaForm(forms.Form):
    merek = forms.CharField(max_length=100)
    stock = forms.IntegerField()
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "size", "price", "thumbnail", "is_featured"]
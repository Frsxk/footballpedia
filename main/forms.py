from django.forms import ModelForm
from main.models import Shop 

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["name", "description", "category", "size", "price", "thumbnail", "is_featured"]
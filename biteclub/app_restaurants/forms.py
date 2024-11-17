from django import forms 
from . import models
from app_common.models import Address

class CreateRestaurant(forms.ModelForm):
    street = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=20, required=True)

    class Meta:
        model = models.Restaurant
        fields = ['name', 'description', 'image']

    def save(self, commit=True):
        restaurant = super().save(commit=False)

        # Save or update the Address separately
        address, created = Address.objects.get_or_create(
            street=self.cleaned_data['street'],
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code']
        )
        restaurant.address = address
        
        if commit:
            restaurant.save()
        return restaurant

class CreateMenuItem(forms.ModelForm):
    class Meta:
        model = models.Menu_Item
        fields = ['name', 'description', 'price', 'photo']
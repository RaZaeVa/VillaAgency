from django import forms
from .models import House


class HouseUpdateForm(forms.ModelForm):

    class Meta:
        model = House
        fields = ('address', 'post_code', 'region', 'category', 'area', 'floor', 'bedroom', 'bathroom', 'parking_lot', 'description', 'authorization_type', 'payment_method', 'price')


class HouseCreateForm(forms.ModelForm):

    class Meta:
        model = House
        fields = (
            'address',
            'category',
            'region',
            'post_code',
            'image',
            'area',
            'floor',
            'bedroom',
            'bathroom',
            'parking_lot',
            'description',
            'is_security',
            'authorization_type',
            'payment_method',
            'price'
        )
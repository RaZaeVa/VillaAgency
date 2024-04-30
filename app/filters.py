import django_filters
from .models import House

class HouseFilters(django_filters.FilterSet):
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = House
        fields = (
            'category',
            'address',
            'region',
            'area',
            'bedroom',
            'bathroom',
            'floor',
            'parking_lot',
            'is_security',
            'authorization_type',
            'payment_method',
        )
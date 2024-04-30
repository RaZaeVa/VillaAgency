from django.contrib import admin
from .models import House, Category, PaymentMethod, Storage


admin.site.register(House)
admin.site.register(Category)
admin.site.register(PaymentMethod)
admin.site.register(Storage)

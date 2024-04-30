from django.urls import path
from . import views


urlpatterns = [
    path('lead_list/', views.lead_list_view, name='lead_list'),
    path('lead_delete/<int:pk>/', views.lead_delete_view, name='lead_delete'),
    path('order_list/', views.storage_list_view, name='order_list')
]
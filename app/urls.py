from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('house_list/', views.HouseListView.as_view(), name='house_list'),
    path('house_detail/<int:pk>', views.house_detail_view, name='house_detail'),
    path('house_update/<int:pk>', views.house_update_view, name='house_update'),
    path('house_delte/<int:pk>', views.house_delete_view, name='house_delete'),
    path('house_create/', views.house_create_view, name='house_create'),
]
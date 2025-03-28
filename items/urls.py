from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView
from .views import request_data

urlpatterns = [
    path('', ItemListView.as_view(), name="item_list"),
    path('create', ItemCreateView.as_view(), name="item_create"),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name="item_update"),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name="item_delete"),
    path('request-data/', request_data, name='request_data'),
]
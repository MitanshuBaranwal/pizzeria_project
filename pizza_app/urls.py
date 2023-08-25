# pizzeria/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('get-price/', views.get_price, name='get_price'),  # get price for an order
    path('create-order/', views.create_order, name='create_order'),  # Create an order
    path('track-order/<int:order_id>/', views.track_order, name='track_order'),  # Track an order by ID
]

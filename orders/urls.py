from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('place-order', views.placeOrder, name="place-order"),
    path('confirm-order', views.confirmOrder, name="confirm-order")
]
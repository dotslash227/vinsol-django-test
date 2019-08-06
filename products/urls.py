from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.AuthPage.as_view(), name="login"),
    path('deal-of-the-day', views.dealPage, name="deal"),
    path('logout', views.logoutView, name="logout"),
]
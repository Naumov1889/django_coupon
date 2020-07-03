from django.urls import path
from .views import index

app_name = "coupon"
urlpatterns = [
    path('', index, name="index"),
]
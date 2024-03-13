from django.urls import path
from . import views

urlpatterns = [
    path("gorden", views.gorden, name="gorden"),
    path("rollet", views.rollet, name="rollet"),
    path("checkout", views.checkout, name="checkout")
]

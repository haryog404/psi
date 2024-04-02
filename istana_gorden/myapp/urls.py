from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("home", views.index, name="index"),
    path("katalog", views.katalog, name="katalog"),
    path("tentang-kami", views.tentangkami, name="tentang-kami")
]
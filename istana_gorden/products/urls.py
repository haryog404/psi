from django.urls import path
from . import views

urlpatterns = [
    path("<str:type>/", views.items, name="items"),
    path("checkout", views.checkout, name="checkout")
]

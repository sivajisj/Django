
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path('register/', views.register_view,name="register"),
]


from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path('register/', views.register_view,name="register"),
    path('login/', views.login_view,name="login"),
    path('logout/', views.user_logout,name="logout"),
    path('dashboard/', views.dashboard,name="dashboard"),
]

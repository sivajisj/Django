
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path('register/', views.register_view,name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.user_logout,name="logout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('create-record/', views.create_record,name="create-record"),
    path('update-record/<int:pk>/', views.update_record,name="update-record"),
    path('delete-record/<int:pk>/', views.delete_record,name="delete-record"),
    path('record/<int:pk>/', views.view_record,name="record"),

]

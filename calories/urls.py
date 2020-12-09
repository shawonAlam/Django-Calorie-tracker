from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogOutPage, name='logout'),
    path('select_food/', views.select_food, name='select_food'),
    path('add_food/', views.add_food, name='add_food'),

    path('update_food/<str:pk>/', views.update_food, name='update_food'),
    path('delete_food/<str:pk>/', views.delete_food, name='delete_food'),

    path('register/', views.RegisterPage, name='register'),
    path('profile/', views.ProfilePage, name='profile'),
]
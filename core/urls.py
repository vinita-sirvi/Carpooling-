from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rides/', views.ride_list, name='ride_list'),
    path('rides/<int:pk>/', views.ride_detail, name='ride_detail'),
    path('rides/create/', views.ride_create, name='ride_create'),
    path('profile/', views.user_profile, name='user_profile'),
]
from .import views
from django.urls import path

urlpatterns = [
    path("admin/", views.index, name='index'),
] 

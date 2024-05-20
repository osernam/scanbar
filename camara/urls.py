from django.urls import path, re_path
from . import views

app_name = "camara"

urlpatterns = [
    path('', views.homeView, name='home'),
   
    
]
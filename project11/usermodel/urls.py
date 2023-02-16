from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserViews , name='form'),
    
]

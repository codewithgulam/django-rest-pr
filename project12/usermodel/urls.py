from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUp , name='signup'),
    path('login/', views.user_login , name='userlogin'),
    path('profile/', views.user_profile , name='profile'),
    
]

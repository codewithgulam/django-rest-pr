from django.urls import path
from crud import views

urlpatterns = [
    path('',views.show),
    path('register/',views.home),
    path('update/<int:id>',views.update),
    path('update/updater/<int:id>',views.updatedata),
    path('delete/<int:id>',views.delete),
]
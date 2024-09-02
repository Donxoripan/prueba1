from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index),
    path('app3Donxoripan/',views.texto),
]
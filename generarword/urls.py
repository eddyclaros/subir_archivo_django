from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('principal',views.principal, name='principal'),
]

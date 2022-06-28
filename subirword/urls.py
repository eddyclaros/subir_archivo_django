from django.urls import path
from . import views

urlpatterns = [
    
    path('subirword/', views.SubirWord.subirword, name='subirword'),
    #path('subir/', views.SubirWord.subirword, name='subirword'),
]

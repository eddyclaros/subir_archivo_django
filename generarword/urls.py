from django.urls import path
from . import views
""" path('',views.inicio, name='inicio'),
    path('principal',views.principal, name='principal'), """
urlpatterns = [
    
    path('', views.publication, name='publication'),
    path('coverletter/export', views.coverletter_export, name='coverletter_export'),

]

from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('ativas', views.ativas, name='ativas'),
    path('passadas', views.passadas, name='passadas'),
    path('formacoes', views.formacoes, name='formacoes')
]

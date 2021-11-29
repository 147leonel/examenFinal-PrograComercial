from django.conf.urls import url
from . import views

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('curso/nuevo/', views.curso_nuevo, name='curso_nuevo'),
    ]
from django.conf.urls import url
from .views import post_list

urlpatterns = [
    #url('home',home)

    #Aqui estamos trayendo data de la BD usando la vista post_List
    url('home',post_list),
]
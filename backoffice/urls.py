from django.conf.urls import url
from . import views

app_name = 'backoffice'

urlpatterns=[
    url(r'^store_index/$', views.store_index, name='store_index'),
    url(r'^store_update/{pk}/$', views.store_update, name='store_update'),
    url(r'^store_delete/{pk}/$', views.store_delete, name='store_delete'),
]

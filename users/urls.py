from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
]

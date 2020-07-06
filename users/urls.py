from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns=[
    url(r'^register/$', views.UserAuth.register, name='register'),
    url(r'^login/$', views.UserAuth.login, name='login'),
    url(r'^logout/$', views.UserAuth.logout, name='logout'),
    url(r'^profile/$', views.UserProfile.view_info, name='profile'),
    url(r'^edit_info/$', views.UserProfile.edit_info, name='edit_info'),
    url(r'^edit_pass/$', views.UserProfile.edit_pass, name='edit_pass'),
]

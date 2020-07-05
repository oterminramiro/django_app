from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'backoffice'

urlpatterns = [
	path('store_show',views.StoreCrud.store_show),
	path('store_add', views.StoreCrud.store_add),
	path('store_edit/<int:id>', views.StoreCrud.store_edit),
	path('store_destroy/<int:id>', views.StoreCrud.store_destroy),
]

from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'backoffice'

urlpatterns = [
	path('organization_show',views.OrganizationCrud.organization_show),
	path('organization_add', views.OrganizationCrud.organization_add),
	path('organization_edit/<int:id>', views.OrganizationCrud.organization_edit),
	path('organization_destroy/<int:id>', views.OrganizationCrud.organization_destroy),


	path('store_show',views.StoreCrud.store_show),
	path('store_show/<int:orgid>',views.StoreCrud.store_show),

	path('store_add', views.StoreCrud.store_add),
	path('store_add/<int:orgid>', views.StoreCrud.store_add),

	path('store_edit/<int:id>', views.StoreCrud.store_edit),
	path('store_destroy/<int:id>', views.StoreCrud.store_destroy),

	path('item_show', views.ItemCrud.item_show),
	path('item_show/<int:storeid>', views.ItemCrud.item_show),

	path('item_add', views.ItemCrud.item_add),
	path('item_add/<int:storeid>', views.ItemCrud.item_add),
	path('item_edit/<int:id>', views.ItemCrud.item_edit),
	path('item_destroy/<int:id>', views.ItemCrud.item_destroy),

	path('order_show', views.OrderCrud.order_show),
	path('order_log/<int:orderid>', views.OrderCrud.order_log),

	path('user_show', views.UserCrud.user_show),
	path('user_add', views.UserCrud.user_add),
	path('user_edit/<int:id>', views.UserCrud.user_edit),
	path('user_destroy/<int:id>', views.UserCrud.user_destroy),

	path('user_org_show/<int:userid>', views.UserCrud.user_org_show),
	path('user_org_add/<int:userid>', views.UserCrud.user_org_add),
	path('user_org_destroy/<int:id>', views.UserCrud.user_org_destroy),
]

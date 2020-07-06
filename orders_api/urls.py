from django.urls import path

from . import views

urlpatterns = [
    path("customer_list/", views.CustomerList.as_view(), name="customer_list"),
    path("customer_list/<int:phone>/", views.CustomerExist.as_view(), name="customer_exist"),
    path("customer_code/", views.CustomerCode.as_view(), name="customer_code"),
    path("customer_login/", views.CustomerLogin.as_view(), name="customer_login"),

    path("item_list/", views.ItemList.as_view(), name="item_list"),
    path("item_list/<int:pk>/", views.ItemExist.as_view(), name="item_exist"),

    path("store_list/", views.StoreList.as_view(), name="store_list"),
    path("store_list/<int:pk>/", views.StoreExist.as_view(), name="store_exist"),

	path("order_create/", views.OrderCreate.as_view(), name="order_create"),
]

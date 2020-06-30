from django.urls import path

from . import views

urlpatterns = [
    path("customer_list/", views.CustomerList.as_view(), name="customer_list"),
    path("customer_list/<int:phone>/", views.CustomerExist.as_view(), name="customer_exist"),
    path("customer_code/", views.CustomerCode.as_view(), name="customer_code"),
    path("customer_login/", views.CustomerLogin.as_view(), name="customer_login"),
    path("item_list/", views.ItemList.as_view(), name="item_list"),
    path("item_list/<int:pk>/", views.ItemExist.as_view(), name="item_exist")
]

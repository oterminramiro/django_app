from django.urls import path

from . import views

urlpatterns = [
    path("create_customer/", views.CreateCustomer.as_view(), name="create_customer"),
    path("find_customer/", views.FindCustomer.as_view(), name="find_customer"),
    path("list_card/", views.ListCard.as_view(), name="list_card"),
    path("save_card/", views.SaveCard.as_view(), name="save_card"),
    path("payment/", views.Payment.as_view(), name="payment"),

    path("save_card_view/", views.SaveCardView.save_card_view, name="save_card_view"),
    path("payment_view/", views.PaymentView.payment_view, name="payment_view"),

]

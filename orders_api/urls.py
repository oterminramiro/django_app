from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'items', views.ItemViewSet, basename="item")
router.register(r'store', views.StoreViewSet, basename="store")
router.register(r'customer', views.CustomerViewSet, basename="customer")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

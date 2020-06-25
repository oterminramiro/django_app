from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'store', views.StoreViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderitem', views.OrderItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

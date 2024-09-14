from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet, OrderViewSet

app_name = 'customers'

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

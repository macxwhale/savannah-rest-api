from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasScope
from .utils import send_sms


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["read", "write", "full_access"]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["read", "write", "full_access"]

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        phone_number = customer.phone
        message = f"New order added: {order.item}, amount: {order.amount}"
        response = send_sms(phone_number, message)
        print(response)

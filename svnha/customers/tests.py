from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        # create sample customers here.
        self.customer = Customer.objects.create(
            name="John Doe",
            code="JD001",
            phone="+254712345678"
        )

    def test_customer_creation(self):
        # Test customer creation
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.code, "JD001")
        self.assertEqual(self.customer.phone, "+254712345678")

    def test_invalid_phone_number(self):
        # Test that an invalid phone number raises a ValidationError
        with self.assertRaises(ValidationError):
            customer = Customer(
                name="Jane Doe",
                code="JD002",
                phone="0712345678"  # Invalid, missing country code
            )
            customer.full_clean()  # Trigger validation

    def test_unique_code_constraint(self):
        # Test that unique constraint on 'code' is enforced
        with self.assertRaises(Exception):
            Customer.objects.create(
                name="Jane Doe",
                code="JD001",  # Duplicate code
                phone="+254700000000"
            )

    def test_unique_name_constraint(self):
        # Test that unique constraint on 'name' is enforced
        with self.assertRaises(Exception):
            Customer.objects.create(
                name="Jane Doe",
                code="JD001",  # Duplicate code
                phone="+254700000000"
            )

class OrderModelTest(TestCase):
    def setUp(self):
        # Set up customer and order objects
        self.customer = Customer.objects.create(
            name="Alice",
            code="AL001",
            phone="+254798765432"
        )
        self.order = Order.objects.create(
            item="Laptop",
            amount=999.99,
            customer=self.customer
        )

    def test_order_creation(self):
        # Test order creation and association with customer
        self.assertEqual(self.order.item, "Laptop")
        self.assertEqual(self.order.amount, 999.99)
        self.assertEqual(self.order.customer, self.customer)

    def test_customer_order_relation(self):
        # Test related_name "orders" is set up correctly
        self.assertEqual(self.customer.orders.count(), 1)
        self.assertEqual(self.customer.orders.first(), self.order)

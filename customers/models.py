from django.db import models
import uuid
import re
from django.core.exceptions import ValidationError


def validate_kenyan_phone_number(phone):
    phone_str = str(phone)
    if not re.match(r"^\+254\d{9}$", phone_str):
        raise ValidationError(
            f"{phone} is not a valid Kenyan phone number. Please include the country code."
        )


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, unique=True)
    phone = models.CharField(
        max_length=13, unique=True, validators=[validate_kenyan_phone_number]
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=200)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.item

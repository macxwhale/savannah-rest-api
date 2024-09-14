from django.db import models
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.name
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=200)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.item

from django.db import models

# Create your models here.


class Delivery(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('T', 'In Transit'),
        ('D', 'Delivered'),
    ]

    order_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=200)
    address = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"


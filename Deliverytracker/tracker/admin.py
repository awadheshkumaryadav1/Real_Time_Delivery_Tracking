from django.contrib import admin

# Register your models here.

from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'status', 'updated_at']
    list_filter = ['status']
    search_fields = ['order_id', 'customer_name']


from django.contrib import admin
from .models import Item, Orderitem, Order, Payment, Refund, Address

# Register your models here.
admin.site.register(Item)
admin.site.register(Orderitem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Refund)
admin.site.register(Address)

from django.contrib import admin

# Register your models here.
from .models import Bag, Item
admin.site.register(Bag)
admin.site.register(Item)

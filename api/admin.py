from django.contrib import admin

# Register your models here.
from .models import Item, Location
admin.site.register(Item)
admin.site.register(Location)
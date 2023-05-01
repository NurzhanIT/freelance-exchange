from django.contrib import admin

from .models import MarketUser


# Register your models here.


@admin.register(MarketUser)
class MarketUserAdmin(admin.ModelAdmin):
    fields = ['username','email',]
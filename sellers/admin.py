from django.contrib import admin

from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields =('name',)


admin.site.register(Seller, SellerAdmin)


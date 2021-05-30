from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'seller', 'price', 'city', 'state')
    list_display_links = ('id', 'title')
    list_filter = ('seller',)
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'state', 'price')
    list_per_page = 30

admin.site.register(Listing,ListingAdmin)

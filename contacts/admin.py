from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','listing','contact_date')
    list_display_links = ('id','name')
    list_per_page = 30
    search_fields = ('name','email','listing')


admin.site.register(Contact, ContactAdmin)

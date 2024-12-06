from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'is_active',
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
    search_fields = ('name', 'email',)
    list_filter = ('is_active',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
admin.site.register(Contact, ContactAdmin)
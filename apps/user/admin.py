from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


admin.site.site_header = "Balita Admin Paneli"
admin.site.site_title = "Balita Admin Paneli"
admin.site.index_title = "Balita Boshqaruv Paneliga Xush Kelibsiz!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'image',
        'is_staff',
        'is_superuser',
        'is_active',
        'last_login',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'last_login',
        "date_joined",
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'description', 'image',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ('created_at', 'updated_at', "date_joined", 'last_login',)
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'description', 'image', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )
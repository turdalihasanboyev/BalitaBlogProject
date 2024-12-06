from django.contrib import admin
from .models import Tag, Category


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    )
    ordering = ('id',)
    search_fields = (
        'name',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    list_filter = (
        'is_active',
        'name',
    )
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    )
    ordering = ('-id',)
    search_fields = (
        'name',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    list_filter = (
        'is_active',
        'name',
    )
    prepopulated_fields = {
        'slug': ('name',),
    }
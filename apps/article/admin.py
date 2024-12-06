from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'image_1',
        'image_2',
        'image_3',
        'author',
        'category',
        'views',
        'for_banner',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'author__first_name',
        'author__last_name',
        'category__name',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_filter = (
        'is_active',
        'for_banner',
        'category__name',
        'created_at',
        'author__first_name',
        'author__last_name',
        'name',
    )


class CommentAdmin(admin.ModelAdmin):
    ordering = ('id',)
    readonly_fields = (
        'id',
        'created_at',
        "updated_at",
    )
    list_display = (
        'id',
        'article',
        'article__category',
        'user',
        'name',
        'email',
        'web_site',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'article__name',
        'user__first_name',
        'user__last_name',
        'name',
        'email',
        'web_site',
    )
    list_filter = (
        'is_active',
        'article__name',
        'article__category__name',
        'user__first_name',
        'user__last_name',
        'name',
        'email',
        'web_site',
        'created_at',
        'updated_at',
    )
admin.site.register(Comment, CommentAdmin)
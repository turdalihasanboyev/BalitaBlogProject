from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import handler404
from .errors import CustomPageNotFoundPageView

urlpatterns = [
    path('balita/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', include('apps.article.urls')),
    path('', include('apps.about.urls')),
    path('', include('apps.user.urls')),
    path('', include('apps.contact.urls')),
    path('', include('apps.common.urls')),
    path('', include('apps.category.urls')),
]

handler404 = CustomPageNotFoundPageView.as_view()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
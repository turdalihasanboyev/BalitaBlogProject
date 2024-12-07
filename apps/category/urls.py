from django.urls import path
from .views import CategoryPageView


urlpatterns = [
    path('category/<slug:slug>/', CategoryPageView.as_view(), name='category'),
]
from django.urls import path
from .views import RegisterPageView, LoginPageView, LogoutView


urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
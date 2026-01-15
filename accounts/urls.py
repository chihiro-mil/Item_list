from django.urls import path
from .views import UserLoginView, register_view

app_name = 'accounts'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
]
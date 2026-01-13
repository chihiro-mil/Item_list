from django.urls import path
from . import UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
]
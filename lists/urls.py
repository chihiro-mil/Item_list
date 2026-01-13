from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.list_index, name='list_index'),
]
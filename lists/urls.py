from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.list_index, name='list_index'),
    #path('<int:list_id>/edit/', views.list_edit, name='list_edit'),
    #path('<int:list_id>/delete/', views.list_delete, name='list_delete'),
]
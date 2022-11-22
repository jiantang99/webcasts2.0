from django.urls import path
from .views import index, destination_detail

app_name='course'

urlpatterns = [
    path('', index, name='destination_list'),
    path('<slug:slug>', destination_detail, name='destination_detail'),
]
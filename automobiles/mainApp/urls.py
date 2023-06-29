from django.urls import path, include
from .views import *

app_name = 'mainApp'
urlpatterns = [
    path('', index, name='index'),
]
from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
]

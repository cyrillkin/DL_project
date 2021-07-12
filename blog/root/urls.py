from django.conf.urls import url
from django.urls import path
from .views import index, test

urlpatterns = [
  path('test/', test, name='test'),
  url('', index, name='index')  
]
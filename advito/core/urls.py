from django.conf.urls import url
from django.urls import path
from .views import index, test

urlpatterns = [
  url('test/', test, name='test'),
  url('', index, name='index'),
  
]

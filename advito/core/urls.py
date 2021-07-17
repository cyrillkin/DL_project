from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
  path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
  path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
  path('posts/create/', views.post_create, name='post_create'),
  path('feed/', views.feed, name='feed'),
]

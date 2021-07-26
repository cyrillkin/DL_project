from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('announcement/', views.announcement, name='announcement'),
    path('adverts/<int:advert_id>/', views.advert, name='advert'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category, name='category'),
    # url(r'^$', views.index, name='index'),
    # url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    # path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    # path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    # path('posts/create/', views.post_create, name='post_create'),
    # path('feed/', views.feed, name='feed'),
]

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'root'

urlpatterns = [
    path('', views.index, name='index'),
    # path('announcement/', views.announcement, name='announcement'),
    # path('adverts/<int:advert_id>/', views.advert, name='advert'),
    # path('cat/', views.cat, name='cat'),
    # path('category/<int:category_id>/', views.category, name='category'),
]

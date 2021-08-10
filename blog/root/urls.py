from django.conf.urls import url
from django.urls import path

from . import views
from auth.urls_auth import urlpattens as auth_patterns


app_name = 'root'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('announce/', views.AnnounceView.as_view(), name='announce'),
    path('adverts/<int:advert_id>/', views.AdvertView.as_view(), name='advert'),
    path('cat/', views.CategoryView.as_view(), name='cat'),
    path('category/<int:category_id>/', views.CategoryViewAdverts.as_view(), name='category'),
    # path('', views.CategoryViewIndex.as_view(), name='cat_index'),

    # path('admin/', views.IndexView.as_view(), name='admin'),
    # path('adverts/<int:advert_id>/', views.advert, name='advert'),
    # path('cat/', views.cat, name='cat'),
    # path('cat/', views.SubCategoryView.as_view(), name='s_cat'),
    # path('category/<int:category_id>/', views.category, name='category'),
]

urlpatterns += auth_patterns

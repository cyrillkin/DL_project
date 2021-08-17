from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views
from auth.urls import urlpattens as auth_patterns


app_name = 'root'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('announce/', views.AnnounceView.as_view(), name='announce'),
    path('adverts/<int:advert_id>/', views.AdvertView.as_view(), name='advert'),
    path('cat/', views.CategoryView.as_view(), name='cat'),
    path('category/<int:category_id>/', views.CategoryViewAdverts.as_view(), name='category'),
    path('adverts/<int:advert_id>/bookmark/', views.AddRemoveView.as_view(), name='bookmark'),
    
    path('adv_create/', views.AdvertCreateView.as_view(), name='adv_create'),
    path('adverts/<int:advert_id>/adv_delete/', views.AdvertDeleteView.as_view(), name='adv_delete'),
    path('adverts/<int:advert_id>/adv_delete_success/', TemplateView.as_view(template_name='root/delete_success.html'), name='delete-adv-success'),
    path('adverts/<int:advert_id>/adv_edit/', views.AdvertCreateView.as_view(), name='adv_edit'),
]

urlpatterns += auth_patterns

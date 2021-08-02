from django.contrib.auth import logout
from django.urls import path

from . import views_auth
from .views_auth import LoginView, logout_view, EditProfileView



urlpattens = [
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', logout_view, name='logout'),
  # path('profile/<int:user_id>', ProfileView.as_view(), name='profile')
  path('profile/<int:user_id>', views_auth.profile, name='profile'),
  path('profile/<int:user_id>/edit/', EditProfileView.as_view(), name='profile-edit'),
]


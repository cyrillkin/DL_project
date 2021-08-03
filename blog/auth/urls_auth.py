from django.urls import path
from django.contrib.auth.views import (
  PasswordResetDoneView, PasswordResetView,
  PasswordResetConfirmView, PasswordResetCompleteView
)

from . import views_auth
from .views_auth import (
  SignUpView, LoginView, logout_view, EditProfileView
)



urlpattens = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', logout_view, name='logout'),
  # path('profile/<int:user_id>', ProfileView.as_view(), name='profile')
  path('profile/<int:user_id>', views_auth.profile, name='profile'),
  path('profile/<int:user_id>/edit/', EditProfileView.as_view(), name='profile-edit'),
]


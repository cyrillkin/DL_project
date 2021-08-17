from django.urls import path
from django.contrib.auth.views import (
  PasswordResetDoneView, PasswordResetView,
  PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls.base import reverse_lazy

from . import views
from .views import (
  SignUpView, LoginView, logout_view, EditProfileView
)


urlpattens = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', logout_view, name='logout'),
  # path('profile/<int:user_id>', ProfileView.as_view(), name='profile'),
  path('profile/<int:user_id>', views.profile, name='profile'),
  path('profile/<int:user_id>/edit/', EditProfileView.as_view(), name='profile-edit'),
  
  path('password_reset/', PasswordResetView.as_view(
    template_name='my_auth/password_reset.html',
    success_url=reverse_lazy('root:password_reset_done')
  ), name='password_reset'),
  
  path('password_reset/done/', PasswordResetDoneView.as_view(
    template_name='my_auth/password_reset_done.html'
  ), name='password_reset_done'),
  
  path('password_reset/<str:uidb64>/<slug:token>', PasswordResetConfirmView.as_view(
    success_url=reverse_lazy('root:password_reset_complete')), name='password_reset_confirm'),

  path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


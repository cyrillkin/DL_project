from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.forms.models import fields_for_model
from django.http import request
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView

from .forms import LoginForm, UpdateProfileForm, SignUpForm
from root.models import Prof


class LoginView(DefaultLoginView):
    template_name = 'my_auth/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('root:index'), request)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('root:login'))


# class ProfileView(DetailView):
#     model = Prof
#     template_name = 'my_auth/profile.html'

#     def get_object(self):
#         return get_object_or_404(self.model, user__id=self.kwargs['user_id'])


def profile(request, user_id):
  """ Детальная страница объявления """

  profile = get_object_or_404(Prof, id=user_id)
  return render(request, 'my_auth/profile.html', {'profile': profile})


class EditProfileView(UpdateView):
    model = Prof
    form_class = UpdateProfileForm
    template_name = 'my_auth/edit_profile.html'
    slug_field = "user_id"
    slug_url_kwarg = "user_id"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise Http404('Ошибка доступа')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        user_id = self.kwargs['user_id']
        return reverse('root:profile-edit', args=(user_id, ))


class SignUpView(View):
    template_name = 'my_auth/signup.html'
    signup_form = SignUpForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.signup_form})

    def post(self, request, *args, **kwargs):
        user_form = self.signup_form(data=request.POST)
        registered = False
        context={}
        if user_form.is_valid():
            user_form.save()
            registered = True
        else:
            context.update({
                'form': user_form
            })
        context.update({
            'registered': registered
            })
        return render(request, self.template_name, context)

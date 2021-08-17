from django.core.exceptions import PermissionDenied

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse

from .models import Adv, Cat, Prof
from .forms import AdvForm


class IndexView(ListView):
    """ Последние 6 опубликованных объявлений """

    model = Adv
    template_name = 'root/index.html'
    context_object_name = 'advert'

    def get_queryset(self):
        return self.model.objects.all().order_by('-date_pub')[:6]


class AnnounceView(ListView):
    """ Все объявления в короткой форме """

    model = Adv
    template_name = 'root/announce.html'
    context_object_name = 'adverts'


class AdvertView(DetailView):
    """ Детальная страница объявления """

    model = Adv
    pk_url_kwarg = 'advert_id'
    template_name = 'root/advert.html'
    context_object_name = 'advert'


class CategoryView(ListView):
    """ Представление с разделением по категориям """

    model = Cat
    template_name = 'root/cat.html'
    context_object_name = 'cat'

    def get_queryset(self):
        return self.model.objects.all()


class CategoryViewAdverts(View):
    """ Страница с разделением по категориям """

    template_name = 'root/category.html'

    def get(self, request, category_id, *args, **kwargs):
        category = Adv.objects.filter(name_cat=Cat.objects.get(id=category_id))
        return render(
            request=request,
            template_name=self.template_name,
            context={'category': category}
        )


class CategoryViewNav(CategoryView):
    """ Представление-навигация"""

    template_name = 'root/nav.html'
    context_object_name = 'nav'


class AdvertCreateView(CreateView):
    """ Представление создания объявления """

    form_class = AdvForm
    template_name = 'root/adv_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.author = request.user
            advert.save()
            return redirect(reverse('root:advert', kwargs={'advert_id': advert.id}))
        else:
            return render(request, 'root/adv_create.html', {'form': form})


class AdvertDeleteView(DeleteView):
    """ Представление удаления объявления """

    model = Adv
    pk_url_kwarg = 'advert_id'
    template_name = 'root/adv_delete.html'

    def get_success_url(self):
        advert_id = self.kwargs['advert_id']
        return reverse('root:delete-adv-success', args=(advert_id, ))


class AdvertUpdateView(UpdateView):
    """ Представление редактирования объявления """

    model = Adv
    pk_url_kwarg = 'advert_id'
    template_name = 'root/adv_edit.html'
    form_class = AdvForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('Вы не автор')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        advert_id = self.kwargs['adv_id']
        return reverse('root:adv', args=(advert_id, ))


class AddRemoveView(View):
    """ Представление добавления в закладки """

    def post(self, request, advert_id, *args, **kwargs):
        advert = get_object_or_404(Adv, id=advert_id)
        if advert in request.advert.bookmark.bookmark.all():
            request.advert.bookmark.bookmark.remove(advert)
        else:
            request.advert.bookmark.bookmark.add(advert)
        return redirect(request.META.get('HTTP_REFERER'), request)


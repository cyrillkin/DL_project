from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Adv, Cat


class IndexView(ListView):
    """ Последние 7 опубликованных объявлений """

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

    def post(self, request, advert_id, *args, **kwargs):
      advert = get_object_or_404(Adv, id=advert_id)
      return render(
        request=request,
        template_name=self.template_name,
        context={'advert': advert}
      )


# def advert(request, advert_id):
#     """ Детальная страница объявления """

#     advert = get_object_or_404(Adv, id=advert_id)
#     return render(request, 'root/advert.html', {'advert': advert})


class CategoryView(ListView):
  """ Представление с разделением по категориям """
  
  model = Cat
  template_name = 'root/cat.html'
  context_object_name = 'cat'

  def get_queryset(self):
    return self.model.objects.all()


def category(request, category_id):
    """ Страница с разделением по категориям """
    
    category = Adv.objects.filter(name_cat=Cat.objects.get(id=category_id))
    return render(request, 'root/category.html', {'category': category})
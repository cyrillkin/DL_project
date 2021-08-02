from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Adv, Cat, Sub_cat


class IndexView(ListView):
    """ Последние 7 опубликованных объявлений """

    model = Adv
    template_name = 'root/index.html'
    context_object_name = 'advert'

    def get_queryset(self):
        return self.model.objects.all().order_by('-date_pub')[:7]


class AnnounceView(ListView):
    """ Все объявления в короткой форме """

    model = Adv
    template_name = 'root/announce.html'
    context_object_name = 'adverts'


# class AdvertView(DetailView):
#     """ Детальная страница объявления """

#     model = Adv
#     pk_url_kwarg = 'advert_id'
#     template_name = 'root/advert.html'

#     def post(self, request, advert_id, *args, **kwargs):
#         advert = get_object_or_404(Adv, id=advert_id)
#         return render(request, self.template_name, {'advert': advert})


def advert(request, advert_id):
    """ Детальная страница объявления """

    advert = get_object_or_404(Adv, id=advert_id)
    return render(request, 'root/advert.html', {'advert': advert})


def cat(request):
  """ Страница с разделением по категориям """

  # adverts = Advert.objects.all().order_by('-date_pub')[:7]
  # return render(request, 'root/cat.html', {'adverts': adverts})
  cat = Cat.objects.all()
  return render(request, 'root/cat.html', {'cat': cat})
        # output = [f'Категория:{category.category_name}' for category in cat]
        # output = [f'id:{advert.id} | Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Дата публикации:{advert.date_pub}' for advert in adverts]

        # output = [f'Категория:{category.category_name} for category in cat']
        # return HttpResponse(output)


def category(request, category_id):
  """ Страница с разделением по категориям """

#   category = get_object_or_404(Cat, id=category_id)
  category = Advert.objects.filter(category=category_id)   
  return render(request, 'root/category.html', {'category': category})
        # sub_categories = Category.objects.filter(sub_category=category_id)
        # output = [f'Категория:{categories.category_name} for category in categories']
        # return HttpResponse(output)
        # return HttpResponse('Здесь будет разделение по категориям')


# def category(request, sub_cat_id):
#   """ Список объявлений разделённых по категориям """

  # adverts = Advert.objects.filter(category=category_id)
  # category = get_object_or_404(Cat, id=category_id)
  # category = Adv.objects.filter(sub_cat=sub_cat)
  # return render(request, 'root/category.html', {'category': category})
  # category = Category.objects.
#   # ID_category:{category.id}
#   output = [f'Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Фото:{advert.photo}' for advert in adverts]
#   return HttpResponse(output)
#   # return HttpResponse(f'Страница с категорией объявления #{category_id}.')

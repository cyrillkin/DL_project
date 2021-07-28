from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Adv, Cat, Sub_cat


def index(request):
#   """ Последние 7 опубликованных объявлений """

  adverts = Adv.objects.all().order_by('-date_pub')[:7]
  return render(request, 'root/index.html', {'advert': adverts})
  
  # output = [f'id:{advert.id} | Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Дата публикации:{advert.date_pub}' for advert in adverts]
  # return HttpResponse(output)
  # return HttpResponse('Последние 7 опубликованных объявлений.')


# def announcement(request):
#   """ Все объявления в короткой форме """

#   adverts = Advert.objects.all()
#   return render(request, 'root/announcement.html', {'adverts': adverts})
  # output = [f'Наименование:{advert.header} | Категория:{advert.category} | Фото:{advert.photo}' for advert in adverts]
  # return HttpResponse(output)
    # return HttpResponse('Здесь будут все объявления в короткой форме.')


# def advert(request, advert_id):
#   """ Детальная страница объявления """

#   advert = get_object_or_404(Advert, id=advert_id)
#   return render(request, 'root/advert.html', {'advert': advert})
  # output = [f'ID:{advert.id} | Создатель:{advert.author} | Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Фото:{advert.photo} | Дата публикации:{advert.date_pub}']
  # return HttpResponse(output)
  # return HttpResponse(f'Объявление #{advert_id}.')


# def cat(request):
#   """ Страница с разделением по категориям """
#   adverts = Advert.objects.all().order_by('-date_pub')[:7]
#   return render(request, 'root/cat.html', {'adverts': adverts})
  # cat = Category.objects.all()
  # return render(request, 'root/cat.html', {'category': cat})
  # output = [f'Категория:{category.category_name}' for category in cat]
  # output = [f'id:{advert.id} | Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Дата публикации:{advert.date_pub}' for advert in adverts]
  
  # output = [f'Категория:{category.category_name} for category in cat']
  # return HttpResponse(output)


# def categories(request):
#   """ Страница с разделением по категориям """
  
#   categories = Category.objects.all()

#   return render(request, 'root/categories.html', {'category': categories})
  # sub_categories = Category.objects.filter(sub_category=category_id)
  # output = [f'Категория:{categories.category_name} for category in categories']
  # return HttpResponse(output)
  # return HttpResponse('Здесь будет разделение по категориям')


# def category(request, category_id):
#   """ Список объявлений разделённых по категориям """

#   adverts = Advert.objects.filter(category=category_id)
#   # category = Category.objects.
#   # ID_category:{category.id}
#   output = [f'Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Фото:{advert.photo}' for advert in adverts]
#   return HttpResponse(output)
#   # return HttpResponse(f'Страница с категорией объявления #{category_id}.')


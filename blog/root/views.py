from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.db.models import Sum

from .models import Advert, Category


def index(request):
  """ Последние 7 опубликованных объявлений """

  adverts = Advert.objects.all().order_by('-date_pub')[:7]
  # output = [f'id:{advert.id} | Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Дата публикации:{advert.date_pub}' for advert in adverts]
  return render(request, 'root/index.html', {'adverts': adverts})
  # return HttpResponse(output)
  # return HttpResponse('Последние 7 опубликованных объявлений.')


def announcement(request):
  """ Все объявления в короткой форме """

  adverts = Advert.objects.all()
  output = [f'Наименование:{advert.header} | Категория:{advert.category} | Фото:{advert.photo}' for advert in adverts]
  return HttpResponse(output)
    # return HttpResponse('Здесь будут все объявления в короткой форме.')


def advert(request, advert_id):
  """ Детальная страница объявления """

  advert = get_object_or_404(Advert, id=advert_id)
  output = [f'ID:{advert.id} | Создатель:{advert.author} | Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Фото:{advert.photo} | Дата публикации:{advert.date_pub}']
  return HttpResponse(output)
  # return HttpResponse(f'Объявление #{advert_id}.')


def categories(request):
  """ Страница с разделением по категориям """
  
  categories = Category.objects.all()
  # sub_categories = Category.objects.filter(sub_category=category_id)
  output = [f'Категория:{category.category_name} for category in categories']
  return HttpResponse(output)
  # return HttpResponse('Здесь будет разделение по категориям')


def category(request, category_id):
  """ Список объявлений разделённых по категориям """

  adverts = Advert.objects.filter(category=category_id)
  # category = Category.objects.
  # ID_category:{category.id}
  output = [f'Наименование:{advert.header} | Категория:{advert.category} | Описание:{advert.description} | Фото:{advert.photo}' for advert in adverts]
  return HttpResponse(output)
  # return HttpResponse(f'Страница с категорией объявления #{category_id}.')

# def index(request):
#   posts = Post.objects.annotate(like_nums = Sum('likes')).order_by('-like_nums')[:10]
#   output = [f'id:{post.id}|description:{post.description}' for post in posts]
#   return HttpResponse(output)
    # return HttpResponse('10 наиболее популярных постов.')

# def feed(request):
#   bookmarks = request.user.user_profile.users_bookmark.all()
#   adverts = Post.objects.filter(author__in=bookmarks)
#   output = [f'id:{post.id}|description:{post.description}' for post in adverts]
#   return HttpResponse(output)
    # return HttpResponse('Лента друзей.')

# def index(request):
#   return HttpResponse('index')

# def post_detail(request, post_id):
#   return HttpResponse(f'Детальное представление поста #{post_id}')

# def post_edit(request, post_id):
#   return HttpResponse(f'Изменение поста поста #{post_id}')

# def post_create(request):
#   return HttpResponse(f'Создание нового поста')

# def post_delete(request, post_id):
#   return HttpResponse(f'Удаление поста #{post_id}')

# def like_post(request, post_id):
#   return HttpResponse(f'Лайкнуть пост #{post_id}')

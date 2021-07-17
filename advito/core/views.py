from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from .models import Post


def index(request):
  posts = Post.objects.annotate(like_nums = Sum('likes')).order_by('-like_nums')[:10]
  output = [f'id:{post_id}|description:{post_description}' for post in posts]
  return HttpResponse(output)

def feed(request):
  return HttpResponse('2')

def post_detail(request, post_id):
  return HttpResponse(f'{post_id}')

def post_edit(request):
  return HttpResponse('4')

def post_create(request):
  return HttpResponse('5')

def post_delete(request):
  return HttpResponse('6')

def like_post(request):
  return HttpResponse('7')
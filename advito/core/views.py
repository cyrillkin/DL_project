from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('1')

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
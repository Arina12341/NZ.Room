
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def page_news(request):
    return render(request, 'page_news.html')

def users(request):
    return render(request, 'users.html')

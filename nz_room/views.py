
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def page_news(request):
    return render(request, 'page_news.html')
def kabinet(request):
    return render(request, 'kabinet.html')

def users(request):
    return render(request, 'users.html')

def my_page(request):
    return render(request, 'mypage.html')

def menu(request):
    return render(request, 'menu.html')


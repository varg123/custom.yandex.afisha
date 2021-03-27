from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('Привет!')

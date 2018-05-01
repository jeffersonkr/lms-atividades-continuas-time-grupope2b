from django.shortcuts import render
from utils.utils import calculaMEdiaFinal
from django.http import HttpResponse

def media(request):
    media= calculaMEdiaFinal(10,8)
    return HttpResponse(media)

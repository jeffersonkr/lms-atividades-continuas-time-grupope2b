from django.urls import path
from core.views import *



urlpatterns = [
    path('', home),
    path('graduacao/', graduacao),
    path('sobrecurso/', sobrecurso),
]

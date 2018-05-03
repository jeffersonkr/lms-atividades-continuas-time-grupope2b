from django.urls import path
from utils.views import media

urlpatterns = [
    path('', media)
]
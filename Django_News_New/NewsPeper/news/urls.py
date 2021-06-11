from django.contrib import admin
from django.urls import path, include
from .views import index, NewsList, NewsDetail, NewsSearch

urlpatterns = [
    #path('index', index),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', NewsSearch.as_view()),
]

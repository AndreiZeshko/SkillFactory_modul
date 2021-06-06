from django.contrib import admin
from django.urls import path, include
from .views import index, NewsList, NewsDetail

urlpatterns = [
    path('index', index),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
]

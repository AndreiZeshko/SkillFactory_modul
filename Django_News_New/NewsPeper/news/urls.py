from django.contrib import admin
from django.urls import path, include
from .views import index, NewsList, NewsDetail, NewsSearch, NewsAdd, NewsDelete, NewsUpdate

urlpatterns = [
    #path('index', index),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news2'),
    path('search/', NewsSearch.as_view()),
    path('add/', NewsAdd.as_view(), name='add'),
    path('create/<int:pk>', NewsUpdate.as_view(), name='update'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='delete'),
]

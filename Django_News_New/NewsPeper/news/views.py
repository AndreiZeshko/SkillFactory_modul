from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, News, Category, Comment, NewsCategory
from datetime import datetime

def index(request):
    return render(request, 'index.html')
# Create your views here.

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'news2.html'
    context_object_name = 'news2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context

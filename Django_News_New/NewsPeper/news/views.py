from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, News, Category, Comment, NewsCategory
from datetime import datetime
from django.views import View
from django.core.paginator import Paginator
from .filters import NewsFilter

def index(request):
    return render(request, 'index.html')
# Create your views here.

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 1

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['category'] = Category.objects.all()
        print(self.request.GET)
        print(context)
        return context

class NewsSearch(ListView):
    model = News
    template_name = 'news_search.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-data')

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'news2.html'
    context_object_name = 'news2'
    paginate_by = 1


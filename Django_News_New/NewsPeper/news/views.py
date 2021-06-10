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
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

    def get(self, request):
        news = News.objects.order_by('-id')
        p = Paginator(news, 1)

        news = p.get_page(request.GET.get('page', 1))
        data = {
            'news': news,
        }
        return render(request, 'news.html', data)

class NewsDetail(DetailView):
    model = News
    template_name = 'news2.html'
    context_object_name = 'news2'
    paginate_by = 1
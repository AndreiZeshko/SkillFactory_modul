from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Author, News, Category, Comment, NewsCategory, BaseRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .filters import NewsFilter
from .forms import NewsForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

class MyView(PermissionRequiredMixin):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

def index(request):
    return render(request, 'index.html')
# Create your views here.

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 5

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
    form_class = NewsForm

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class NewsAdd(CreateView, PermissionRequiredMixin):
    model = News
    template_name = 'news_add.html'
    context_object_name = 'news'
    form_class = NewsForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)

class NewsDetail(DetailView):
    model = News
    template_name = 'news2.html'
    context_object_name = 'news2'
    queryset = News.objects.all()


class NewsUpdate(UpdateView):
    template_name = 'news_add.html'
    context_object_name = 'news'
    form_class = NewsForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'news/login.html'


# дженерик для удаления товара
class NewsDelete(DeleteView):
    template_name = 'delete.html'
    queryset = News.objects.all()
    success_url = '/news/'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')
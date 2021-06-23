from django.contrib import admin
from django.urls import path, include
from .views import index, NewsList, NewsDetail, NewsSearch, NewsAdd, NewsDelete, NewsUpdate, ProtectedView, BaseRegisterView, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('index', index),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news2'),
    path('search/', NewsSearch.as_view()),
    path('add/', NewsAdd.as_view(), name='add'),
    path('create/<int:pk>', NewsUpdate.as_view(), name='update'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='delete'),
    path('', ProtectedView.as_view()),
    path('login/',
         LoginView.as_view(template_name = 'login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'logout.html'),
         name='logout'),
    path('newsup/',
         BaseRegisterView.as_view(template_name = 'newsup.html'),
         name='newsup'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('upgrade/', upgrade_me, name = 'upgrade')
]

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models import Sum

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

class Author(models.Model):
    user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True)
    ratingAuthor = models.IntegerField(default=0)

    def rating(self):
        newsRat = self.news_set.aggregate(newsRating=Sum("рейтинг"))
        nRat = 0
        nRat += newsRat.get("рейтинг новости")

        commentRat = self.comment_set.aggregate(commentRating=Sum("рейтинг"))
        cRat = 0
        cRat += commentRat.get("рейтинг коментария")

        self.ratingAuthor = nRat * 3 + nRat
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Category(models.Model):
    category = models.CharField(max_length=30, unique=True, verbose_name='Категория')
    text = models.TextField(blank=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class News(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Категория')
    heading = models.CharField(max_length= 30, unique=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Автор')
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    rating = models.IntegerField(default=0)

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def preview(self):
        prew = self.text[0:123] + "..."
        return prew

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.NewsCategory

    class Meta:
        verbose_name = 'категории новостей'
        verbose_name_plural = 'категории новостей'

class Comment(models.Model):
    commentNews = models.ForeignKey(News, on_delete= models.CASCADE)
    commentUser = models.ForeignKey(Author, on_delete= models.CASCADE)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

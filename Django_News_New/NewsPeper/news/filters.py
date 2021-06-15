import django_filters
from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import News, Category
from django import forms
import django_filters

# создаём фильтр
class NewsFilter(FilterSet):

    data = django_filters.DateFilter(
        field_name='data',
        widget=forms.DateInput(attrs={'class': 'data', 'class': 'from-control'}),
        lookup_expr='gt',
    )



    heading = django_filters.CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
    )
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = News
        fields = [
            'data',
            'author',
            'heading',
            'category'
        ]  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
from django.forms import ModelForm, BooleanField
from .models import News



class NewsForm(ModelForm):
    check = BooleanField(label='Проверка')
    class Meta:
        model = News
        fields = ['heading', 'author', 'category', 'text', 'check']

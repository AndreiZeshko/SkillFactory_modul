from django.forms import ModelForm, BooleanField
from .models import News
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class NewsForm(ModelForm):
    check = BooleanField(label='Проверка')
    class Meta:
        model = News
        fields = ['heading', 'author', 'category', 'text', 'check']


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
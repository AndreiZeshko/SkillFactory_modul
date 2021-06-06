from django import template

register = template.Library()

STOP_LIST = [
    'мат',
]

@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')

#@register.filter(neme='mat')
#def mat(text='news.text'):
    #for text in text:
        #if text in STOP_LIST:
            #text = '(CENSORED)'
        #return text
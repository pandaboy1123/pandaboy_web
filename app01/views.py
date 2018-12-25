from django.shortcuts import render
from app01.models import *


# Create your views here.
def loading(request):
    return render(request, 'loading.html')


def index(request):
    date_obj = Blog.objects.all()
    date_list = []
    score_list = []
    for obj in date_obj:
        date_list.append(obj.date)
        score_list.append(obj.score)
    date_list.reverse()
    score_list.reverse()
    return render(request, 'index.html', locals())

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
    return render(request, 'articles/index.html', context={'tags': tags, 'article_id': article_id})
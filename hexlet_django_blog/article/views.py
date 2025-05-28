from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        mess = messages.get_messages(request)
        return render(
            request,
            'articles/index.html',
            context={
                'articles':articles,
                'messages': mess,
                },
        )
        
        
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={
                'article': article,
            },
        )
        
        
class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request, 'articles/create.html', {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Статья успешно создана')
            return redirect(reverse('article_index'))
        messages.add_message(request, messages.ERROR, 'Ошибки')
        return render(request, 'articles/create.html', {'form': form})
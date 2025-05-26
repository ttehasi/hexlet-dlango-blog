from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.urls import reverse


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'who':'World', 'more': args, **kwargs})
    
    
def about(request):
    return render(request, 'about.html')
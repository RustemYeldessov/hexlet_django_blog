from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class ArticleIndexView(View):
    def get(self, request, tags, article_id):
        context = {
            'tags': tags,
            'article_id': article_id,
        }
        return render(request, 'articles/index.html', context)


class HomeRedirectView(View):
    def get(self, request):
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)
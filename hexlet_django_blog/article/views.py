from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html')
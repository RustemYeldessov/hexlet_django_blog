from django.urls import path
from hexlet_django_blog.article.views import ArticleIndexView, HomeRedirectView

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home'),
    path('articles/<str:tags>/<int:article_id>/', ArticleIndexView.as_view(), name='article'),
]
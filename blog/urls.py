from .views import Home, Article, ArticleDetails
from django.urls import include, path

urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view()),
    path('articles/<int:id>', ArticleDetails.as_view())

]
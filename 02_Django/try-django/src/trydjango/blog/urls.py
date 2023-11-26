from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleListView,
    ArticleDeleteView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'), #kw_arg as pk by default on detail
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]


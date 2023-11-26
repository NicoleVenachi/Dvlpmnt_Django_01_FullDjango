from django.shortcuts import render

from .models import Article

from django.views.generic import (
  CreateView, 
  UpdateView,
  ListView,
  DetailView,
  DeleteView,
)
# Create your views here.

class ArticleListView(ListView): #list several
  template_name = 'articles/article_list.html' # ovewrite the template name

  queryset = Article.objects.all() #necesito pasar un queryset con la data para listar


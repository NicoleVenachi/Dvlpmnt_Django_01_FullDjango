from django.shortcuts import render, get_object_or_404

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

class ArticleDetailView(DetailView): #list several
  template_name = 'articles/article_detail.html' # ovewrite the template name

  def get_object(self):
    id_ = self.kwargs.get('id') 
    return get_object_or_404(Article, id=id_) #element to show

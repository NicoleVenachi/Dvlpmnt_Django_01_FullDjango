from django.shortcuts import render, get_object_or_404

from django.views.generic import (
  CreateView, 
  UpdateView,
  ListView,
  DetailView,
  DeleteView,
)

from .models import Article
from .forms import ArticleModelForm

# Create your views here.

class ArticleCreateView(CreateView): #list several
  template_name = 'articles/article_create.html' # ovewrite the template name
  form_class = ArticleModelForm # set te form
  # success_url = '/'
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
  # def get_success_url(self):
  #   return '/'
  
class ArticleUpdateView(UpdateView): #list several
  template_name = 'articles/article_create.html' # ovewrite the template name
  form_class = ArticleModelForm # set te form
  # success_url = '/'
  

  def get_object(self):
    id_ = self.kwargs.get('id') 
    return get_object_or_404(Article, id=id_) #element to show

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  

class ArticleListView(ListView): #list several
  template_name = 'articles/article_list.html' # ovewrite the template name

  queryset = Article.objects.all() #necesito pasar un queryset con la data para listar

class ArticleDetailView(DetailView): #list several
  template_name = 'articles/article_detail.html' # ovewrite the template name

  def get_object(self):
    id_ = self.kwargs.get('id') 
    return get_object_or_404(Article, id=id_) #element to show

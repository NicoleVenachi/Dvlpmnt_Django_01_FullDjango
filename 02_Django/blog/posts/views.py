from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.all() # queryng all the posts
  #print(posts)
  return render(request, 'index.html', {'posts': posts})

def post(request, pk):
  post = Post.objects.get(id=pk) #queryng ONE post, by id
  return render(request, 'posts.html', {'posts': post})
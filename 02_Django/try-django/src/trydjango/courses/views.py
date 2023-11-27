from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course 
# BASE VIEW CLass = VIEW

# Create your views here.


class CourseCreateView(View):
  
  template_name = "courses/course_create.html" # DetailView
  def get(self, request, *args, **kwargs):
    # GET method to fetch the form UI
    form = CourseModelForm()
    context = {"form": form}
    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    # POST method, to crete an onbect instancee through the form
    form = CourseModelForm(request.POST)
    if form.is_valid():
        form.save()
        form = CourseModelForm()
    context = {"form": form}
    return render(request, self.template_name, context)



class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self): # to looks closer than the generic view does
      return self.queryset

    def get(self, request, *args, **kwargs):
      context = {'object_list': self.get_queryset()}
      
      return render(request, self.template_name, context)
    

class CourseView(View): #or course detail view
    template_name = "courses/course_detail.html" # DetailView

    #id =None, argumen is not longer required, none by default
    def get(self, request, id=None, *args, **kwargs):
      # GET method
      if id is not None:
        obj = get_object_or_404(Course, id=id)
      context = {'object': obj}
      # context = {'object': self.get_object()}
      return render(request, self.template_name, context)


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course 
# BASE VIEW CLass = VIEW

# Create your views here.

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
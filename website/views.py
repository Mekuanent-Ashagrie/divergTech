from django.shortcuts import render
from .models import Course
from django.views import generic

class HomeView(generic.ListView):
    model = Course
    template_name = 'website/home.html'
    context_object_name = "course_list"
    
    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by("-course_name")[:5]
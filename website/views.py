from django.shortcuts import render
from .models import Course
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Member

class HomeView(generic.ListView):
    model = Course
    template_name = 'website/home.html'
    context_object_name = "course_list"
    
    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by("-course_name")[:5]
    
def addmember(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    member = Member(member_name = name, member_email = email, member_phone = phone, member_message = message)
    member.save()
    return HttpResponseRedirect(reverse('home'))
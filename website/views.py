from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Member, Event, Software, Testimonial, Partner

class HomeView(generic.ListView):
    model = Course
    template_name = 'website/home.html'
    context_object_name = "course_list"
    
    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by("-course_name")[:5]
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.order_by("-event_name")[:5]
        context['software_list'] = Software.objects.order_by("-software_name")[:5]
        context['testimonial_list'] = Testimonial.objects.order_by("-client_name")[:5]
        context['partner_list'] = Partner.objects.order_by("-partner_name")[:5]
        return context
    
def addmember(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    member = Member(member_name = name, member_email = email, member_phone = phone, member_message = message)
    member.save()
    return HttpResponseRedirect(reverse('home'))
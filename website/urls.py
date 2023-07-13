from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('home', views.HomeView.as_view(), name='Home'),
]

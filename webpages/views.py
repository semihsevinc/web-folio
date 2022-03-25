from django.shortcuts import render
from .models import BlogModel
# Create your views here.

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request , 'home.html' , context)

def base(request):
    return render(request , 'base.html')

def about(request):
    return render(request , 'about.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def home(request):
    users=User.objects.all()
    return render(request,"app1/index.html",{'users':users})
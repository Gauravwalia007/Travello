from django.shortcuts import render,redirect
from .models import Destination

def index(request):
    
    dest=Destination.objects.all()

    return render(request,'index.html',{'dests':dest})



from django.shortcuts import render,redirect,HttpResponse
#from .models import UserProfile
from django.contrib import messages
from .forms import RegistrationForm,EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

def home(request):
    return redirect('/')


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
        else:
            return render(request,'register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request,'register.html',{'form':form})



def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})


def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile'))
        # else:
        #     return render(request,'editprofile.html',{'form':form})
    else:
        form = EditProfileForm(instance=request.user)
        return render(request,'edit_profile.html',{'form':form})

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:login'))
        # else:
        #     return render(request,'change_password.html',{'form':form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'change_password.html',{'form':form})
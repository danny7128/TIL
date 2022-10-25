from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect(request, 'accounts:index')
    

def follow(request,user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if request.user == user:
        return redirect('accounts:profile', user_pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile',user_pk)    

def profile(request,user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        'user':user
    }
    return render(request, 'accounts/profile.html', context)
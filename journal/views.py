from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'journal/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            send_mail('Edenthought Project','Welcome to our Application and we are glad that you are here and joined our program',settings.DEFAULT_FROM_EMAIL,[current_user.email])
            profile = Profile.objects.create(user=current_user)
            messages.success(request,'User Created Successfully..')
            return redirect('login')
    return render(request,'journal/register.html',{'form':form})

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    return render(request,'journal/login.html',{'form':form})

@login_required(login_url='login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    return render(request,'journal/dashboard.html',{'profile_pic':profile_pic})

def log_out(request):
    auth.logout(request)
    messages.success(request,'User logged out Successfully..')
    return redirect('')

@login_required(login_url='login')
def create_thought(request):
    form = ThoughtForm()
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            messages.success(request,'Thought Created Successfully..')
            return redirect('my-thoughts')
    return render(request,'journal/createThought.html',{'form':form})

@login_required(login_url='login')
def my_thoughts(request):
    current_user = request.user.id
    thoughts = Thoughts.objects.all().filter(user = current_user)
    return render(request,'journal/myThoughts.html',{'thoughts':thoughts})

@login_required(login_url='login')
def update_thought(request,pk):
    try:
        thought = Thoughts.objects.get(id=pk,user = request.user)
    except:
        return redirect('my-thoughts')
    form = ThoughtForm(instance=thought)
    if request.method == 'POST':
        form = ThoughtForm(request.POST,instance=thought)
        if form.is_valid():
            form.save()
            messages.success(request,'Thought updated Successfully..')
            return redirect('my-thoughts')
    return render(request,'journal/updateThought.html',{'form':form})

@login_required(login_url='login')
def delete_thought(request,pk):
    try:
        thought = Thoughts.objects.get(id=pk,user=request.user)
    except:
        return redirect('my-thoughts')
    if request.method == 'POST':
        thought.delete()
        messages.success(request,'Thought deleted Successfully..')
        return redirect('my-thoughts')
    return render(request,'journal/deleteThought.html')

@login_required(login_url='login')
def profile(request):
    form = UpdateUSerForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)
    form_2 = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateUSerForm(request.POST,instance=request.user)
        form_2 = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        if form_2.is_valid():
            form_2.save()
            return redirect('dashboard')
    return render(request,'journal/profile.html',{'form':form,'form_2':form_2})

@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()
        return redirect('')
    return render(request,'journal/deleteAccount.html')
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, Change_details
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'home/home.html')

def register(requset):
    if requset.method == 'POST':
        form = RegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse("please enter valid details")
    else:
        form = RegisterForm()
        return render (requset, 'home/register.html', {'form':form})
    
def Login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("User is not found!")
    else:
        form = LoginForm()
        return render (request, 'home/login.html', {'form':form})
    

def Logout(request):
    logout(request)
    return redirect ('login')


@login_required
def details_change(request):
    if request.method == 'POST':
        form = Change_details(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("enter valid details!!") 
    else:
        form = Change_details(instance=request.user)
        return render (request, 'home/update.html', {'form':form})  
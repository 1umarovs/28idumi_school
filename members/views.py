from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '{} login successfully'.format(user.username))
            return redirect('main:homePage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request,'registration/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('main:homePage')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, '{} registered successfully'.format(user.username))
            return redirect('main:homePage')
    else:
        form = RegisterUserForm()
    
    return render(request,'registration/register.html' , {'form':form})
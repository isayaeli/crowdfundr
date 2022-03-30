import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

def request_login(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successful Logged In')
            return redirect('home')
        messages.error(request, 'Username or password is Incorrect!')
        return redirect('login')
        
    return render(request,  'userauth/login.html')
             

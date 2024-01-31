from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

def login_view_old(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return render(request, 'add_lab_processing.html', {})

    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return render(request, 'accounts/login.html', {})
        
    return render(request, 'accounts/logout.html', {})

def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('index') 
        else:
            messages.error(request, 'Invalid username or password.')
            context = {"error": "Invalid username or password."}

    return render(request, 'accounts/login.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'{user_name} logged in successfully')
            return redirect('home')
        else:
            messages.warning(request, f'username or password incorrect')
    return render(request, 'app/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')

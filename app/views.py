from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_page(request) -> render:
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'{user_name} logged in successfully')
            return redirect('loggedin')  # Corrected redirection
        else:
            messages.warning(request, 'Username or password incorrect')
    return render(request, 'app/login.html')


def successfully_logged_in(request) -> render:  # Corrected function name
    return render(request, 'app/successfully.html')  # Corrected template filename


def logout_user(request) -> redirect:
    logout(request)
    return redirect('login')

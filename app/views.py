from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app.models import Posts
from django.contrib.auth.decorators import login_required


def login_page(request):
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

@login_required(login_url='login')
def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})


@login_required(login_url='login')
def announcements(request):  # Corrected function name
    posts = Posts.objects.all()

    context = {
        "post": posts
    }
    return render(request, 'app/home.html', context)  # Corrected template filename


def logout_user(request):
    logout(request)
    return redirect('login')

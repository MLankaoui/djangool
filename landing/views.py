from django.shortcuts import render

def home(request) -> render:
        return render(request, "landing/index.html")

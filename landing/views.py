from django.shortcuts import render
from django.http import HttpResponse

def home(request) -> HttpResponse:
        return HttpResponse("<h1>Home page<h1>")

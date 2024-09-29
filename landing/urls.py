from django.urls import path
from landing.views import home

urlpatterns = [
    path ('', home, name="home")
]
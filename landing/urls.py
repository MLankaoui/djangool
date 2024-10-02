from django.urls import path
from landing.views import home
from app.views import login_page

urlpatterns = [
    path ('', home, name="home"),
    path('login/', login_page, name="login")
]
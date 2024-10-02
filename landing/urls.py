from django.urls import path
from landing.views import home
from app.views import login_page, successfully_logged_in

urlpatterns = [
    path ('', home, name="home"),
    path('login/', login_page, name="login"),
    path('logged_in/', successfully_logged_in, name="loggedin")
]
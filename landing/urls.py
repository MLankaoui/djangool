from django.urls import path
from landing.views import home
from app.views import login_page, successfully_logged_in, logout_user

urlpatterns = [
    path ('', home, name="home"),
    path('login/', login_page, name="login"),
    path('announcements/', successfully_logged_in, name="loggedin"),
    path('logout/', logout_user, name='logout')
]
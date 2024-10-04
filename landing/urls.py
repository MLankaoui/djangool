from django.urls import path
from landing.views import home
from app.views import login_page, announcements, logout_user, post_detail

urlpatterns = [
    path ('', home, name="home"),
    path('login/', login_page, name="login"),
    path('announcements/', announcements, name="loggedin"),
    path('logout/', logout_user, name='logout'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
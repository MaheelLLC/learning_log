"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register'),
]

# Let's talk about the new urlpattern in login page. LoginView is a class-based 
# view provided by Django to handle user authentication and login.
# LoginView.as_view() sets up the login view where now the template is an
# argument for this method.
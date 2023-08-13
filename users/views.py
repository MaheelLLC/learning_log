from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

# To make our life easy, Django already comes with a logout function that
# we can call from within the view right here. See, we need to provide a way 
# for users to log out. We won't build a page for logging out; users will
# just click a link and be sent back to the home page. We define a URL pattern
# for the logout link, write a view function, and provide a logout link in
# base.html. Thus, we don't need render, context, or even an html argument
# like before.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)

# In the register function, we check the POST conditional again. If it's a GET 
# request, we make an instance of UserCreationForm with no initial data. If we 
# get a POST request instead, we make an instance of UserCreationForm based on 
# the submitted data. If the submitted data is valid, we call the form's save() 
# method to save the username and the hash of the password to the database. The 
# save() method returns the newly created user object which we store in 
# new_user. After all this, we log them in, which is a two step process: we 
# call authenticate() with the arguments new_user.username and password. When 
# they register, the user is asked to enter two matching passwords, and because 
# the form is valid, we know the passwrods match, so we can use either one. 
# Here we get the value associated with the 'password1' key in the form's POST 
# data. If the username and password are correct, the method returns an 
# authenticated user object, which we store in authenticated_user. We then call 
# the login() function with the request and authenticated_user objects which 
# creates a valid session for the new user.
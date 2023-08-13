from django.contrib import admin

# Register your models here.

# Django allows you to create a type of user called a superuser. A superuser
# has all priveleges available on the site. A privilege controls the actions
# a user can take. The most restrictive privilege settings allows a user to only
# read public information on the site.

# When you define models for an app, Django makes it easy for you to work with 
# your models through the admin site. A site's administrators use the admin 
# site, not a site's general users.

# Here's what you type in the virtual environment terminal to create a
# superuser
# python3 manage.py createsuperuser
# Username: ll_admin (admin name)
# Email address: (whatever email)
# Password: (whatever password you want)
# Password (again): (same password)

# Fun fact: Django doesn't actually store your password that you enter; instead
# it stores a string derived from the password called a hash. Each time you
# enter your password, Django hashes your entry and compares it to the stored
# hash. If they match, you're authenticated.

# To register Topic with the admin site, enter:

from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

# This code imports the model we want to register, Topic, and then uses
# admin.site.register() to tell Django to manage our model through the admin
# site.

# We need to register the Entry model so we added admin.site.register(Entry).
# When we say register, we mean to put the model in the admin site for editing
# purposes. It actually shows up on the admin site when you register it.

# Admin
# username: ll_admin
# password Titeecoo1308$$
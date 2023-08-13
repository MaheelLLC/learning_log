"""Defines URL patterns for learning_logs."""

# from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    # url(r'^$', views.index, name = 'index'),
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, 
         name = 'edit_entry'),
]

# We add a docstring at the top to make it clear which urls file we're working
# on. We then import the url function (path does the same) which is needed
# when mapping URLs to views. We also import the views module; the dot tells
# Python to import views from the same directory as the current urls.py module
# This means that views is literally in the same folder. The variable
# urlpatterns in this module is a list of individual pages that can be
# requested from the learning_logs app. The actual URL pattern is a call to the
# url() function, which takes 3 arguments. The first is a regular expression
# (r'^$'). This defines the pattern that Django can look for. r tells Python
# to interpret the following string as a raw string, and the quotes tell
# Python where the regular expression begins and ends. The caret ^ tells Python
# to find the beginning of the string, and the dollar sign $ tells Python to
# find the end of the string. In its entirety, the expression tells Python to
# look for a URL with nothing between the beginning and end of the URL.
# Python ignores the base URL for the project (http://localhost:8000/) so an
# empty regular expression matches the base URL. The second argument specifies
# which view function to call. The third argument just gives the url pattern
# a name called index. Whenever we want to provide a link to the home page,
# we'll just call index instead of writing out the URL.

# When building a website, you'll almost always require some elements to be
# repeated on each page. This is why we create a base template for these
# repeated elements and then have each page inherit from the base template.
# Our parent template is called base.html.
# In html, you use two spaces instead of four for nesting/indenting.
# If you look at base.html, you'll notice something called a template tag which
# is used to generate a link on the web page. The template tag is indicated by
# curly braces and percent signs {% %}. A template tag is a bit of code that
# generates information to be displayed on a page.
# For example, template tag {% url 'learning_logs:index' %} generates a URL
# matching the URL pattern defined in learning_logs/urls.py with the name
# 'index'.
# In index.html, the {% extends %} tag on the first line tells Django which
# parent template the index child template is inheriting from. In this case,
# it is base.html. 

# (?P<topic_id>\d+)/ matches an integer between two forward slashes and stores
# the integer value in an argument called topic_id. The parentheses
# surrounding this part of the expression captures the value stored in the URL
# the ?p<topic_id> part stores the matched value in topic_id; and the 
# expression \d+ matches any number of digits that appear between the forward
# slashes.
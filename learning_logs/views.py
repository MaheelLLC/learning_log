from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

# A view function takes in information from a request, prepares the data needed
# to generate a page, and then sends the data back to the browser, often
# by using a template that defines what the page will look like.
# This file imports the render() function which renders the response based on
# the data provided by views.
# When a URL request matches the pattern we defined in urls.py (same folder).
# Django will look for a function called index in this file. Django then passes
# the request object to this view function. The render() function takes two
# arguments: the original request object and a template (the .html string)

# At topics = Topic.object.order_by('date_added'), we're querying the database
# by asking for the Topic objects in the order of the date_added attribute.
# At the next line, we define a context that we'll send to the template. A 
# context is a dictionary in which the keys are names we'll use in the template
# to access the data and the values are the data we need to send to the
# template.

# The topic function gets the topic and all associated entries from the
# database. Remember, when we put in urls int:topic_id? This function accepts
# the value captured by the expression int:topic_id. We use get() to retrieve
# the topic just as it was done in the Django shell. We get entries associated
# with this topic and we order them according to date_added: the minus sign
# in front of date_added sorts the results in reverse order, which will display
# the newest entries first. We store the topic and entries in the context
# dictionary and send context to the template topic.html

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# We import the class HttpResponseRedirect which is used to redirect a reader
# back to the topics page after they submit their topic. The reverse() function
# determines the URL from a named URL pattern, meaning that Django will generate
# the URL when the page is requested.

# The two main types of request you'll use when building web apps are GET
# requests and POST requests. You use GET requests for pages that only read
# data from the server. You usually use POST requests when the user needs to
# submit information through a form. The function new_topic() takes in the
# request object as a parameter. When the user initially requests this page,
# their browser will send a GET request. When the user has filled out and
# submitted the form, their browser will submit a POST request.

# This is why we said request.method != 'POST'. If the request doesn't equal
# POST, it most likely equals GET, so we need to return a blank form.
# We make an instance of TopicForm, store it in variable form, and send the
# form to the template in the context dictionary. No arguments in
# instantiating TopicForm, so Django is gonna create a blank form for the user.
# If the request method is POST, we make an instance of TopicForm and pass it
# the data entered by the user, stored in request.POST. The form object that's
# returned contains the information submitted by the user.

# We can't save the submitted information in the database until we've checked
# that it's valid. The is_valid() function does this job and makes sure that
# form fits the constraints from the Topic model.

# Let's talk about the new_topic.html / template here. In the first new line,
# the action argument tells the server where to send the data submitted in
# the form; in this case, we send it back to the view function new_topic().
# The method argument tells the browser to submit the data as a POST request.
# The template tage {% csrf_token %} to prevent attackers from using the form
# to get unauthorized access to the server. In the line after, we diplay the
# actual form. The as_p modifier tells Django to render all the form elements
# in paragraph format, which is a simple way to display the form neatly.
# We also made our own button in the last line.
# Now, we'll link this new page to the topics page.

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# The definition of new_entry() has a topic_id parameter to store the value it
# receives from the URL.

# Ok, we know that the else block is for POST requests. Once the POST form is
# valid, we need to set the entry object's topic attribute before saving it
# to the database. Thus, when we call save(), we include the argument
# commit=False to tell Django to create a new entry objetc and store it in
# new_entry without saving it to the database yet. We then set new_entry's
# topic to the topic from the beginning of the function. Then, we finally save
# it.

# Oh yeah, this whole time, did you know that the reverse function requires
# two arguments - the name of the URL pattern we want to generate a URL for
# and an args list containing any arguments that need to be included in the
# URL.

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# This view function will render the edit entry page. Thus, it has some new
# features. I have come to believe that a form is just a nice copy of the
# original model, meaning that it shares its attributes and methods.
# The argument instance = entry tells Django to make an instance of the
# EntryForm and create the form instance prefilled with information from
# the existing entry object.
# The second time that the instance=entry argument shows up is when the user
# edits an entry. In this case, form has two arguments (entry and request.POST).
# They tell Django to create a form insatnce based on the information
# associated with the existing entry object, updated with any relevant data
# from request.POST. 

# Remember keyword and non-keyword arguments? Let's get a refresher.
# A keyword argument is an parameter that gets explicitly defined. For example,
# For exameple, my_function(parameter = 'argument') has a keyword argument
# where the parameter was explicitly defined as 'argument'. A non-keyword
# argument is just a positional argument. You list the arguments in the
# function call and match its order with the parameters of your choice.
# For example, my_function('argument') is a non-keyword argument. To tie this
# lesson in, I'm gonna bring up a new concept entirely called the decorator.
# A decorator is a "wrapper" that wraps around a function, class etc. to change
# a function for an instance without actually changing its definition. In other
# words, a decorator is a directive placed just before a function definition
# that Python applies to the function before it runs to alter how the function
# code behaves. We're gonna use the @login_required decorator to change the
# topics function, so that it only runs for logged in users.

def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404
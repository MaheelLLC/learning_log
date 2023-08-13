from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
# Page 404 of textbook will explain alot of this
# But I will too:
# Let's start from the beginning:
# To work with Django, we have to set up a virtual environment. A virtual 
# environment is a place in your computer where you can install packages and 
# isolate them form all other Python packages. Separating one project's 
# libraries from other projects is crucial which is why the virtual environment 
# exists.
# To make one, you go to your project's directory in your terminal and type
# python3 -m venv ll_env

# venv is a module that creates a virtual environment for us called ll_env

# To activate the virtual environment (which is just entering it), we type
# source ll_env/bin/activate (you can replace ll_env with any virtual
# environment name)

# The command runs the script activate in ll_env/bin.
# In your virtual environment, you have to install Django with 
# pip install Django

# Now that everything is set up, we can actually make a project in Django
# we do this by staying in the virtual environment and typing
# django-admin startproject project_name

# In the project, there will be a settings.py which controls how Django
# interacts with your system and manages your project.

# The urls.py tells Django which pages to build in response to browser requests
# The wsgi.py file helps Django serve the files it creates. It stands for
# web server gateway interface

# Django stores most info related to a project in a database. To make one
# we type:
# python3 manage.py migrate

# Any time we modify a database, we say we're migrating the database. Writing
# migrate for the first time tells Django to make sure that the database
# matches the current state of the project.

# You'll notice a db.sqlite3 file in your project. SQLite is a database that
# runs off a single file. The database is now easy to manage.
# You can run your website by typing:
# python3 manage.py runserver

# A Django project is actually a group of individual apps that work together
# to make the project work as a whole.
# To make an app, you type (still in the virtual environment):
# python3 manage.py startapp app_name

# startapp tells Django to create the infrastructure needed to build an app
# Inside the app file, you'll find models.py, admin.py, and views.py
# models.py is used to define the data we want to manage in our app.

# For our learning log, each entry needs a topic/title which is why in this
# file we create a topic class that inherits from the Model class.
# It has two attributes text and date_added but no init method (weird)
# The models.CharField() method is a piece of data that's made up of
# characters, or text. You use CharField for storing small amounts of text like
# a title or name.

# models.DateTimeField is a piece of data that will record the date and time.
# The argument auto_add_now = True tells Django to automatically set this
# attribute to the current date and time whenever a user creates a new topic

# When we run our website and type on firefox/web browser
# http://localhost:8000/admin/ (replace localhost:8000 with the link given 
# when you run the server, you enter the admin site for the website. Here
# we can add topics and users and just control the site as a whole.

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

# When we add a topic, we need to define a model for the kinds of entries that
# go into said topic. For example, if the topic is chess, we want our users
# to write down their own comments/entries about chess. Each entry needs to be
# associated with a particular topic. This relationship is called a
# many-to-one relationship, meaning many entries can be associated with one
# topic.

# The Entry class inherits from Django's basic Model class, just as Topic did
# before. The first attribute, topic, is a ForeignKey instance. A foreign key
# is a database term. Specifically, it's a reference to another record in the
# database. This is the code that connects each entry to a specific topic. 
# Each topic is assigned a key, or ID, when it's created. When Django needs to
# establish a connection between two pieces of data, it uses a key associated
# with each piece of information. We'll use these connections to retrieve all
# entries associated with a particular topic.

# The next attribute is called text which is an instance of TextField. This
# kind of field doesn't need a size limit, because we don't want to limit the
# size of individual entries. The date_added attribute allows us to present
# the entries in the order they were created and to place a timestamp next to
# each entry.

# We nest the Meta class inside our Entry class. Meta holds extra information
# for managing a model; here it allows us to set a special attribute telling
# Django to use Entries when it needs to refer to more than one entry. Without
# this, Django would call them Entrys.

# The __str__() method tells Django which information to show when it refers
# to individual entries. Because an entry can be pretty long, we're only gonna
# the first 50 characters with ... afterwards.

# Because we've added a new model, we need to migrate the database again.
# This process will become quite familiar: you modify models.py, run the command
# python3 manage.py makemigrations app_name, and then run the command
# python3 manage.py migrate

# Since we entered some data such as topics and entries, we can examine the
# data through an interactive terminal session. This interactive environment is
# called the Django shell. The shell is used for testing and troubleshooting
# your project. To run the shell, type:
# python3 manage.py shell
# To test a certain model such as Topic, you type:
# from app_name.models import model_name 
# (Ex. from learning_logs.models import Topic)
# To see Topic's instances, you type:
# Topic.objects.all()
# The list of instances that is returned by the terminal is called a queryset
# Remember when we connected Entry and Topic through ForeignKey. Django
# can use this connection in the shell to get every entry related to a certain
# topic, like this:
# t = Topic.objects.get(id=1)
# t.entry_set.all
# The structure to access a foreign key model like Entry is the lowercase
# name of the model (entry in this case) followed by an underscore and the
# word set.
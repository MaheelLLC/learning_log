"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('learning_logs.urls','learning_logs'),
                     namespace = 'learning_logs')),
    path('users/', include(('users.urls', 'users'), namespace = 'users')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('learning_logs.urls', namespace = 'learning_logs'))
]

# Usually, making web pages with Django consists of three stages: defining URLs,
# writing views, and writing templates. First, you msut define patterns for
# URLs. A URL pattern describes the way the URL is laid out and tells Django
# what to look for when matching a browser request with a site URL so it knows
# which page to return.
# Each URL then maps to a particular view- the view function retrievesa and
# processes data needed for the page. The view function often calls a template,
# which builds a page that a browser can read.

# Mapping a URL: Users request pages by entering URLs into a browser and
# clicking links, so we'll need to decide what URLs are needed in our
# project. 

# We imported the functions and modules that manage URLs for the project and
# admin site.The urlpatterns variable includes sets of URLs from the app in the 
# project. admin.site.urls defines all URLs that can be requested from the
# admin site.

# We added a namespace argument which allows us to distinguish learning_logs's 
# URLs from other URls that might appear in the project.

# path and url do the same thing. They just have different syntax.

# For every app, we need to attach a url pattern to the app. Now, we have 
# a users app for user registration and authorization and to allow people
# to register an account and log in and out.
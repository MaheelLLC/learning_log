from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
# To allows users to interact with the page, we created a python file that
# imports the topic model and forms module from Django.
# We define a class called TopicForm, which inherits from ModelForm.
# The simplest version of a ModelForm consists of a nested Meta class telling
# Django which model to base the form on and which fields to include in the
# form. In this scenario, we're building a form from the Topic model and
# including only the text field. The labels line tells Django not to generate
# a label for the text field.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# Here's the entry form. Just like the topic form, this one has nearly the same
# beginning. However, we now also have widgets attribute. A widget is an HTML
# form element, such as a single-line text box, multi-line text area, or
# drop-down list. By including this widget attribute, you override Django's
# default widget choices. By telling Django to use forms.Textarea element, we're
# customizing the input widget for the field 'text' so the text area will be
# 80 columns wide instead of the default 40.
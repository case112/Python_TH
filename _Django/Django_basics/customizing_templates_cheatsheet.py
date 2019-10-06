#Refresher

{% for x in y %} - For loop in Django templates

{% extends "template.html" %} - #Causes the current template to extend the quoted template so you can override blocks in the parent template.

{% block name %}{% endblock %} - #Marks the start and end of a named block which can be replaced with inheritance.

{% load static from staticfiles %} - #Loads the {% static %} tag from the staticfiles library.

{% static "/path/to/file.ext" %} - #Generates the URL to the specified file.

wordcount - #Counts the words (defined by whitespace) in the variable.

truncatewords:X - #Ends the variable after X words and appends an ellipsis if any content was cut off.

urlize - #Converts HTTP(S) and email addresses into HTML anchor tags with appropriate links.

#template is Django's module for all things template-related. We'll use this several times in the course.

template.Library is a class that lets us register new tags and filters through an instance of itself.

register.simple_tag(tag_name) or @register.simple_tag - Registers a function as a simple tag. Simple tags don't include new templates, don't have an end tag, and don't assign values to context variables.
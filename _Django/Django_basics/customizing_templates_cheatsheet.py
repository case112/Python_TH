Refresher

{% for x in y %} - For loop in Django templates

{% extends "template.html" %} - Causes the current template to extend the quoted template so you can override blocks in the parent template.

{% block name %}{% endblock %} - Marks the start and end of a named block which can be replaced with inheritance.

{% load static from staticfiles %} - Loads the {% static %} tag from the staticfiles library.

{% static "/path/to/file.ext" %} - Generates the URL to the specified file.


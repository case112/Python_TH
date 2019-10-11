from django.shortcuts import render

from . import forms

def hello_world(request):
    return render(request, 'home.html')


def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST) #request.POST acts kinda like a dictionary
		print('good form1')
		if form.is_valid():
			print('good form2')
	return render(request, 'suggestion_form.html', {'form': form} )
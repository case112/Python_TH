from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from django.shortcuts import render

from . import forms

def hello_world(request):
    return render(request, 'home.html')


def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST) #request.POST acts kinda like a dictionary
		if form.is_valid():
			send_mail(
				'Suggestion form {}'.format(form.cleaned_data['name']),
				form.cleaned_data['suggestion'],
				'{name} <{email}>'.format(**form.cleaned_data),
				['learning_site@email.com']
			)
			messages.add_message(request, messages.SUCCESS,
								'Thanks for your suggestion!')
			return HttpResponseRedirect(reverse('suggestion'))
	return render(request, 'suggestion_form.html', {'form': form} )
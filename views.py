import requests
from django.http import HttpResponse
from django.shortcuts import render



def about(request):
	print ('about')
	return render(request, "about.html")
	
def index(request):
	print ('index')
	return render(request, "index.html")
	
def portfolio(request):
	print ('portfolio')
	response = requests.get('https://api.github.com/users/nishantseoni/repos')
	repos = response.json()
	context = {
        'github_repos': repos,
        	 }
	return render(request, 'portfolio.html', context)

def contact(request):
	print ('contact')
	return render(request, "contact.html")



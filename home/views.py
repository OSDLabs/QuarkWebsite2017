from django.shortcuts import render

# Create your views here.

def home(request):
	if request.user.is_authenticated():
		username= request.user.username
		context = {
		"username" : username,
		}

	context = {}

	
	
	return render(request,"index.html",context)

def speakers(request):
	context = {}
	return render(request, "speakers.html", context)

def exhibits(request):
	context = {}
	return render(request, "exhibits.html", context)

def nites(request):
	context = {}
	return render(request, "nites.html", context)

def team(request):
	context = {}
	return render(request, "team.html", context)

def about(request):
	context = {}
	return render(request, "about.html", context)

def ca(request):
	context = {}
	return render(request, "ca.html", context)

def sponsor(request):
	context = {}
	return render(request, "sponsor.html", context)
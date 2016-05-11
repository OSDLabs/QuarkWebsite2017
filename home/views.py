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

# @login_required
# def Profile(request):
# 	if request.user.is_authenticated():
# 		if not request.use.is_staff():
# 			
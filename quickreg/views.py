from django.shortcuts import render, redirect
from .forms import *
from .models import *

def quickreg(request):
	form = QuickForm()
	if request.method == 'POST':
		if form.is_valid():
			form = QuickForm(request.POST)
			print(request.POST.get('name'))
			obj = quick(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				mobile = request.POST.get('mobile'),
				institute = request.POST.get('institute'),
				gender = request.POST.get('gender'),
				year = request.POST.get('year'),
				panel_des = str(request.POST.getlist('panel_des')),
				panel_elixir = str(request.POST.getlist('panel_elixir')),
				panel_robo = str(request.POST.getlist('panel_robo')),
				panel_prog = str(request.POST.getlist('panel_prog')),
				panel_specials = str(request.POST.getlist('panel_specials')),
				panel_init = str(request.POST.getlist('panel_init')),
				panel_elect = str(request.POST.getlist('panel_elect')),
				panel_corporate = str(request.POST.getlist('panel_corporate')),
				workshop = str(request.POST.getlist('workshop'))
				)
			obj.save()
			print('Success')
			return redirect('home')

	context = {
		'form' : form,
	}
	return render(request, 'quick_reg.html', context)
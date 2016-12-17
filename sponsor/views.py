from django.shortcuts import render
from .models import *
from django.template.defaulttags import register

cat_names = {}

def sponsors(request):
	cat = []
	for i in SPONS:
		cat.append(i[0])
		cat_open = Sponsor.objects.filter(types= i[0]).order_by('order')
		event_props = []
		for j in cat_open:
			event_prop = {}
			event_prop["order"] = j.order
			event_prop["desc"] = j.desc
			event_prop["link"] = j.link
			event_prop["img"] = j.img
			event_props.append(event_prop)
		cat_names[i[0]] = event_props
	# print(cat_names)
	context = {
		"category" : cat,
		"cat":cat_names
		}
	return render(request, "front_spons.html",context)

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def fullf(eventtype):
	return 'Individual' if eventtype == 'S' else 'Team'

@register.filter
def checkoffset(catlist, catitem):
	if len(catlist)%2 and catlist.index(catitem)==0:
		return True
	else:
		return False
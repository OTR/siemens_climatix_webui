from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

from monitor.models import TempVolModel

from scripts.populate_db import tz, rand_float
from random import randint
from datetime import datetime

# Create your views here.

class IndexView(TemplateView):
	template_name = "monitor/index.html"

class ListTempVolView(ListView):
	"""Fetch all the records and display them in a form of HTML table"""
	template_name = "monitor/temp_vol.html"
	model = TempVolModel

# class LatestView(View):
def latest_view(request):
	"""Return Latest rows on each Unit in JSON representation"""
	data = dict()
	names = TempVolModel.CVU_NAME.values
	for name in names:
		rand_vol_intake = randint(17000, 41000)
		data[name] = {
						"temp_intake": rand_float(18.0, 22.0), # A bunch of magic numbers
                        "temp_exhaust": rand_float(26.0, 29.0), # Taken down due to natural
                        "hum_intake": rand_float(60.0, 90.0), # discovering
                        "hum_exhaust": rand_float(30.0, 50.0),
                        "vol_intake": rand_vol_intake,
                        "vol_exhaust": rand_vol_intake-1400, # Intake and exhaust volumes are linked
                        "CVU_name": name,
                        "datetime": datetime.now(tz)
					  }

	# def get_queryset(self):
	# 	"""Return the last 16 rows. One for each unit"""
	# 	return TempVolModel.objects.order_by('-datetime')[:16]

	return JsonResponse(data, safe=True)
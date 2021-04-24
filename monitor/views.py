from django.shortcuts import render
from django.views.generic import ListView
from monitor.models import TempVolModel
# Create your views here.

class IndexView(ListView):
	template_name = "monitor/index.html"
	model = TempVolModel
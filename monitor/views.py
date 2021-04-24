from django.shortcuts import render
from django.views.generic import DetailView, View
from monitor.models import TempVolModel
# Create your views here.

#class IndexView(DetailView):
#	model = TempVolModel
class IndexView(View):

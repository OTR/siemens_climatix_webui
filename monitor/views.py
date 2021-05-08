from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, HttpResponse

from monitor.models import TempVolModel

from scripts.populate_db import tz, rand_float
from random import randint
from datetime import datetime

from scripts import proof

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
        key = proof.CONFIG["translate"][name]
        mySess = proof.MySession(_id=key)
        params = mySess.main_menu_pretty()
        data[name] = {
                        "temp_intake": params["temp_intake"],
                        "temp_exhaust": params["temp_exhaust"],
                        "hum_intake": params["hum_intake"],
                        "hum_exhaust": params["hum_exhaust"],
                        "vol_intake": params["vol_intake"],
                        "vol_exhaust": params["vol_exhaust"],
                        "CVU_name": name,
                        "datetime": datetime.now(tz)
                      }

    return JsonResponse(data, safe=True)

def crash_history_view(request):
    """Display all crash entries for a certain cvu"""
    if request.method == "GET":
        cvu = request.GET.get("cvu")
        if cvu is not None:
            if cvu == "":
                return HttpResponse("Empty string")
            if cvu in "0123456789ABCDEF":
                history = proof.main(mode="crash_hist_once", cvu=cvu)
                content = "\n".join(history)

                return HttpResponse(content, content_type='text/plain; charset=utf8')
            else:
                return HttpResponse("You may need to pick correct id for cvu")

        else:
            return HttpResponse("You need to add 'cvu' param")
    else:
        return HttpResponse("")
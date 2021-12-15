"""
Views for displaying current AHU state and crash history.
"""
from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from monitor.models import TempVolModel
from services import poll_web_server
from services.populate_db import UTC3_TIME_ZONE


class IndexView(TemplateView):
    """Dynamic (via javascript XHR) page for looking at AHU status."""
    template_name = "monitor/index.html"


class ListTempVolView(ListView):
    """Fetch all the records and display them in a form of HTML table."""
    template_name = "monitor/temp_vol.html"
    model = TempVolModel


def latest_view(request):
    """Return Latest rows on each Unit in JSON representation."""
    data = dict()
    ahu_ids = TempVolModel.AhuName.values
    # FIXME: don't make web requests in a view
    for ahu_id in ahu_ids:
        # FIXME: get IP settings from config
        ahu_name = poll_web_server.AHU_IPS[ahu_id].name
        my_sess = poll_web_server.PLCWebClient(ahu_id=ahu_id)
        params = my_sess.main_menu_pretty()
        data[ahu_id] = {
            "temp_intake": params["temp_intake"],
            "temp_exhaust": params["temp_exhaust"],
            "hum_intake": params["hum_intake"],
            "hum_exhaust": params["hum_exhaust"],
            "vol_intake": params["vol_intake"],
            "vol_exhaust": params["vol_exhaust"],
            "AHU_name": ahu_name,
            "datetime": datetime.now(UTC3_TIME_ZONE)
        }

    return JsonResponse(data, safe=True)


def crash_history_view(request):
    """Display all crash entries for a certain AHU."""
    if request.method == "GET":
        ahu_id = request.GET.get("ahu")
        if not ahu_id:
            return HttpResponse("You need to add 'ahu' param")
        if ahu_id not in "0123456789ABCDEF":  # TODO if in AHU_IP.keys()
            return HttpResponse("You may need to pick correct id for ahu",
                                content_type='text/plain; charset=utf8')
        # FIXME: main doesnt return anything
        history = poll_web_server.main(run_mode="crash_hist_once", ahu=ahu_id)

        return render(request,
                      "monitor/crash_history.html",
                      context={
                          "history": history,
                          # FIXME: get IP settings from config
                          "ahu_name": poll_web_server.AHU_IPS[ahu_id].name
                      }
                      )
    else:
        return HttpResponse("")

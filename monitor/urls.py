from django.urls import path
from monitor.views import IndexView, ListTempVolView, latest_view

urlpatterns = [
	path("", IndexView.as_view(), name="index"),
	path("list", ListTempVolView.as_view(), name="temp_vol"),
	path("latest", latest_view, name="latest"),

]
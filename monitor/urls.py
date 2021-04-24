from django.urls import path
from monitor.views import IndexView

urlpatterns = [
	path("", IndexView.as_view(), name="index")
]
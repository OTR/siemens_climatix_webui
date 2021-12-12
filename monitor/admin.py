"""Groups are not used so unregister them."""
from django.contrib import admin
from django.contrib.auth.models import Group

from monitor.models import TempVolModel


admin.site.unregister(Group)
admin.site.register(TempVolModel)

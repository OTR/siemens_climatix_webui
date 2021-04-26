from django.db import models
from datetime import datetime, timezone, timedelta
from django.utils.translation import gettext_lazy as gtl

# Create your models here.
def get_start_epoch():
	"""return 01.01.1970 date with UTC+3 timezone"""

	_date =  datetime.fromtimestamp(0.0)
	tz = timezone(timedelta(hours=3)) # TODO: get rid of hardcoded timezone
	_date_with_tz = _date.replace(tzinfo=tz)
	return _date_with_tz

class TempVolModel(models.Model):
	""""""
	class CVU_NAME(models.TextChoices):
		"""'F' stands for 16 as number in hexadecimal representation"""
		CVU_1_1 = "0", gtl("ЦВУ 1.1")
		CVU_1_2 = "1", gtl("ЦВУ 1.2")
		CVU_1_3 = "2", gtl("ЦВУ 1.3")
		CVU_1_4 = "3", gtl("ЦВУ 1.4")
		CVU_2_1 = "4", gtl("ЦВУ 2.1")
		CVU_2_2 = "5", gtl("ЦВУ 2.2")
		CVU_2_3 = "6", gtl("ЦВУ 2.3")
		CVU_2_4 = "7", gtl("ЦВУ 2.4")
		CVU_3_1 = "8", gtl("ЦВУ 3.1")
		CVU_3_2 = "9", gtl("ЦВУ 3.2")
		CVU_3_3 = "A", gtl("ЦВУ 3.3")
		CVU_3_4 = "B", gtl("ЦВУ 3.4")
		CVU_4_1 = "C", gtl("ЦВУ 4.1")
		CVU_4_2 = "D", gtl("ЦВУ 4.2")
		CVU_4_3 = "E", gtl("ЦВУ 4.3")
		CVU_4_4 = "F", gtl("ЦВУ 4.4")

	# FIXME: make CVU_name and datetime fields not NULL
	# FIXME: CVU_name and datetime unique together

	CVU_name = models.CharField(max_length=1, choices=CVU_NAME.choices,
								default=CVU_NAME.CVU_1_1)
	temp_intake = models.FloatField() # TODO: DecimalField ???
	temp_exhaust = models.FloatField()
	hum_intake = models.FloatField()
	hum_exhaust = models.FloatField()
	vol_intake = models.IntegerField()
	vol_exhaust = models.IntegerField()

	datetime = models.DateTimeField(default=get_start_epoch())

	def get_name(self):
		"""return readable name of Unit"""
		return f"{self.CVU_NAME(self.CVU_name).label}"

	def get_datetime(self):
		"""return readable datetime when smaple was taken"""
		return f"{self.datetime.strftime('%d.%m.%Y %H:%M')}"

	def __str__(self):
		"""Return ЦВУ 1.1 2004.06.03 23:50"""
		return self.get_name() + " " + self.get_datetime()

"""
Models for storing AHU state.
"""
from datetime import datetime, timezone, timedelta

from django.db import models
from django.utils import timezone as _timezone
from django.utils.translation import gettext_lazy


def get_epoch_start_time():
    """Return 01.01.1970 date with UTC+3 timezone"""
    start_time = datetime.fromtimestamp(0.0)
    tz = timezone(timedelta(hours=3))  # TODO: get rid of hardcoded timezone
    date_with_tz = start_time.replace(tzinfo=tz)
    return date_with_tz


class TempVolModel(models.Model):
    """A model that represents AHU state at the moment of polling."""

    class AhuName(models.TextChoices):
        """
        'F' stands for 16 as number in hexadecimal representation
        Since we have only 16 units,
        `CharField` is the smallest data type to fit with.
        """
        AHU_1_1 = "0", gettext_lazy("ЦВУ 1.1")
        AHU_1_2 = "1", gettext_lazy("ЦВУ 1.2")
        AHU_1_3 = "2", gettext_lazy("ЦВУ 1.3")
        AHU_1_4 = "3", gettext_lazy("ЦВУ 1.4")
        AHU_2_1 = "4", gettext_lazy("ЦВУ 2.1")
        AHU_2_2 = "5", gettext_lazy("ЦВУ 2.2")
        AHU_2_3 = "6", gettext_lazy("ЦВУ 2.3")
        AHU_2_4 = "7", gettext_lazy("ЦВУ 2.4")
        AHU_3_1 = "8", gettext_lazy("ЦВУ 3.1")
        AHU_3_2 = "9", gettext_lazy("ЦВУ 3.2")
        AHU_3_3 = "A", gettext_lazy("ЦВУ 3.3")
        AHU_3_4 = "B", gettext_lazy("ЦВУ 3.4")
        AHU_4_1 = "C", gettext_lazy("ЦВУ 4.1")
        AHU_4_2 = "D", gettext_lazy("ЦВУ 4.2")
        AHU_4_3 = "E", gettext_lazy("ЦВУ 4.3")
        AHU_4_4 = "F", gettext_lazy("ЦВУ 4.4")

    # FIXME: make AHU_name and datetime fields not NULL
    # FIXME: AHU_name and datetime unique together

    AHU_name = models.CharField(max_length=1,
                                choices=AhuName.choices,
                                default=AhuName.AHU_1_1
                                )  # VARCHAR(1)
    temp_intake = models.FloatField()  # TODO: DecimalField ???
    temp_exhaust = models.FloatField()  # REAL
    hum_intake = models.FloatField()
    hum_exhaust = models.FloatField()
    vol_intake = models.IntegerField()  # INTEGER
    vol_exhaust = models.IntegerField()

    datetime = models.DateTimeField(default=get_epoch_start_time())

    def get_name(self) -> str:
        """Return verbose name of a Unit."""
        return self.AhuName(self.AHU_name).label

    def get_local_datetime(self) -> str:
        """
        Return readable datetime when sample was taken. i.g.,
        `26.04.2021 15:08 UTC` => `06.05.2021 18:08 MSK`
        """
        local_dt = _timezone.localtime(self.datetime)
        return local_dt.strftime('%d.%m.%Y %H:%M')

    def __str__(self) -> str:
        """
        Return verbose name combined with local time for database record. i.g.,
        `ЦВУ 1.1 2004.06.03 23:50`
        """
        return self.get_name() + " " + self.get_local_datetime()

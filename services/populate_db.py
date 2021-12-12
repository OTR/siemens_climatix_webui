"""
A helper script for filling up database table with random records.
It is used on preparation stage before running tests.
"""
import os
from datetime import datetime, timezone, timedelta
from random import randint, random

# These imports and variable assignations are in the right order
# Don't change them!
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test_settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from monitor.models import TempVolModel


UTC3_TIME_ZONE = timezone(timedelta(hours=3))  # UTC+3


def get_rand_float(_min: int, _max: int) -> float:
    """
    Generate float in between specific given boundaries. Get rid of extra
    decimal numbers. Remain only 1 number after floating point.

    :param _min: lower bound
    :param _max: upper bound
    :return: a pseudo random floating point number
    """
    float_num = _min + (_max - _min) * random()
    fixed_float_num = round(float_num * 10.0) / 10.0

    return fixed_float_num


if __name__ == "__main__":
    # FIXME: There should be context manager for ORM
    try:
        ahu_names = TempVolModel.AhuName.values
        samples = []
        for name in ahu_names:
            rand_vol_intake = randint(17000, 41000)
            samples.append(
                # A bunch of magic numbers taken down due to natural discovering
                TempVolModel(temp_intake=get_rand_float(18, 22),
                             temp_exhaust=get_rand_float(26, 29),
                             hum_intake=get_rand_float(60, 90),
                             hum_exhaust=get_rand_float(30, 50),
                             vol_intake=rand_vol_intake,
                             # Intake and exhaust have constant relationship
                             vol_exhaust=rand_vol_intake - 1400,
                             AHU_name=name,
                             datetime=datetime.now(UTC3_TIME_ZONE)  # FIXME: tz doesnt work
                             )
            )
        TempVolModel.objects.bulk_create(samples)
    except Exception as err:
        print(err)
        raise err

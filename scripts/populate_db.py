from datetime import datetime, timezone, timedelta
import os
import sys
from pathlib import Path
from random import randint, random

tz = timezone(timedelta(hours=3)) # UTC+3
# dt = datetime(2016,5,10,12,30,0,0, tzinfo=tz)
# datetime = datetime.now(tz)

def rand_float(_min, _max):
    """ Generate a pseudo random floating point number
     in between specific given minimum and maximum values"""

    float_num = _min + (_max - _min) * random()
    # get rid of extra decimal numbers. Remain only 1 number after floating point
    fixed_float_num = round(float_num * 10.0) / 10.0
    return fixed_float_num


# ADD our project dir to PYTHONPATH in order to find cvu.settings module
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))

os.environ["DJANGO_SETTINGS_MODULE"] = "cvu.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from monitor.models import TempVolModel

if __name__ == "__main__":
    try:
        names = TempVolModel.CVU_NAME.values
        samples = []
        for name in names:
            rand_vol_intake = randint(17000, 41000)
            samples.append(
                TempVolModel(temp_intake=rand_float(18.0, 22.0), # A bunch of magic numbers
                                        temp_exhaust=rand_float(26.0, 29.0), # Taken down due to natural
                                        hum_intake=rand_float(60.0, 90.0), # discovering
                                        hum_exhaust=rand_float(30.0, 50.0),
                                        vol_intake=rand_vol_intake,
                                        vol_exhaust=rand_vol_intake-1400, # Intake and exhaust volumes are linked
                                        CVU_name=name,
                                        datetime=datetime.now(tz) # FIXME: tz doesnt work
                                        )
                )
        TempVolModel.objects.bulk_create(samples)
    except Exception as e:
        print(e)
        raise e

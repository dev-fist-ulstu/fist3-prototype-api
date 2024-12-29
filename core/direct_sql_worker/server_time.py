import datetime

import pytz
from django.conf import settings
from django.db import connection

def get_server_time_now():
    """Return server time now

    :return: server time
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT NOW()")
        row = cursor.fetchone()
        timezone = pytz.timezone(settings.LOCAL_TIMEZONE)
        time = datetime.datetime.strptime(str(row[0])[:-6], "%Y-%m-%d %H:%M:%S.%f").astimezone(timezone)
    return time
import os

import django
from django.apps import apps
from django.conf import settings

if not apps.ready and not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fred.settings')
    django.setup()

from time import sleep
from django.db import connection



def wait_for_database():
    while True:
        if db_is_ready():
            return
        sleep(0.5)

def db_is_ready():
    try:
        connection.ensure_connection()
        print('Database is ready')
        return True
    except Exception as e:
        print(f'Database is not ready: \n{e}')
        return False


if __name__ == '__main__':
    wait_for_database()


#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djecommerce.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
<<<<<<< HEAD
            "Could not import Django. deneme için bişiler yazıyorum. Are you sure it's installed and "
=======
            "Couldn't really import Django. Are you sure it's installed and "
>>>>>>> 6dec8979997711b422811ac9cd33634e7a924b03
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

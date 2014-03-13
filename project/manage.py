#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname

if __name__ == "__main__":
    sys.path.append('/home/domains/agro')
    sys.path.append('/home/domains/agro/apps')
    SITE_ROOT = dirname(dirname(abspath(__file__)))
    sys.path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

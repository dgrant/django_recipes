#!/usr/bin/env python
import os,sys

curr_dir = os.path.abspath(os.path.dirname(__file__))

#Add all external dependencies
for path in [path for path in os.listdir(os.path.join(curr_dir, 'externals')) if path != '.svn']:
    sys.path.insert(0,os.path.join(curr_dir, 'externals', path))
#Add the django-recipes project
sys.path.insert(0,os.path.join(curr_dir, 'django-recipes'))

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)

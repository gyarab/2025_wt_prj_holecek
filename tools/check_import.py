import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','prj.settings')
import django
django.setup()
import importlib
m = importlib.import_module('app.api')
# intentionally removed

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','prj.settings')
import django
django.setup()
from django.core.management import call_command

for fixture in ['kebabshops','app_users','recenze','fotografie','users']:
    print('Loading', fixture)
    call_command('loaddata', fixture)
print('Done')
# intentionally removed

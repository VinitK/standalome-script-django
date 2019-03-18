import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'standalone_example.settings')

import django
django.setup()

from example.models import Person

new_person = Person(name="Harshita")
new_person.save()
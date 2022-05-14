import os
import sys

try:
    os.system(f'python manage.py startapp {sys.argv[1]}')

    dr = os.path.abspath(os.path.dirname(__file__)) + '/' + sys.argv[1]
    print(dr)

    with open(f'{dr}/forms.py', 'w') as f:
        f.write("""from django import forms
    from django.forms import ModelForm
    from django.contrib.auth.models import User

    #register your forms here
        """)

    with open(f'{dr}/urls.py', 'w') as f:
        f.write("""from django.urls import path
    from . import views

    #register your urls here

    urlspatterns = []
    """)
except FileNotFoundError as e:

    print('Please install django first')

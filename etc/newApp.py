import os

with open('urls.py', 'w') as f:
    f.write("""
from django.urls import path,include
from . import views

urlpatterns = []
    """)


with open('forms.py', 'w') as f:
    f.write("""
from django import forms
import .models as model
""")

os.mkdir('templates')
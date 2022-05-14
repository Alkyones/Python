with open('urls.py', 'w') as f:
    f.write("""
from django.urls import path,include
from . import views

urlpatterns = []
    """)
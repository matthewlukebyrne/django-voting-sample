from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
]
# Need to bring this info into main urls.py!
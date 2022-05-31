from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='quality'),

# Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
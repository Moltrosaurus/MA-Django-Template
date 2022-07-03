# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from apps.qualityend.urls import urlpatterns as qualityend_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    #ADD NEW Routes HERE
   path("", include("apps.qualityend.urls")),  # <----- NEW APP / Qualityprediction

    #Leave 'Home.Urls' as last the last line
    path("", include("apps.home.urls"))             # UI Kits Html files

]
urlpatterns += qualityend_urlpatterns


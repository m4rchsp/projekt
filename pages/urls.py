from django.urls import path, include, re_path
from django.shortcuts import render
from .views import home, index




urlpatterns = [

    path('', home), # / - root
    path('index/', index),
    # re_path(r"^$", home),

]
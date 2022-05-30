"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.shortcuts import render
from projekt.views import home, about

# HTTP REQUEST
from projekt import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    #path('inventory/', include('inventory.urls')), # /inventory/
    path('inventory/', include('inventory.urls')), # /inventory/
    path('about/', about), # /about/
    path('', include('pages/urls.py')), # / - root
    # re_path(r"^$", home),

]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__', include('debug_toolbar.urls')),
#     ] + urlpatterns
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

def show_toolbar(request):
    return True

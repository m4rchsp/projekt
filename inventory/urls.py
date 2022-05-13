"""projekt URL Configuration """


from django.urls import path, include, re_path
from .views import inventory_home2

from django.http import HttpResponse


    # HTTP REQUEST
    # def about(request):
        # HTTP RESPONSE
        # return HttpResponse("ABOUT")


urlpatterns = [

    path('', inventory_home2),

]

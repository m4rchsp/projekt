from django.urls import path

# my imports
from .views import *

urlpatterns = [
    # address , view.as_view(), name

    path('', index.as_view(), name='index')

]

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inventory_home(request):
    # http response
    return HttpResponse( '''<!DOCTYPE>
                                <html>
                                    <head>
                                    </head>
                                    <body>
                                        <p>INVENTORY</p>
                                    </body>
                                </html>
                            ''')

def inventory_home2(request):
    return render(request,'inventory/home.html')


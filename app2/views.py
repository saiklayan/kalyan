from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kalyan(request):
    return HttpResponse('bad boy')

def pranay(request):
    return HttpResponse('<marquee><h1>pranay is a innocent boy like this he was thinking</h1></marquee>')

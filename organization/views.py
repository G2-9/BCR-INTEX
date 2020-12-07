from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'organization/index.html')

def searchOrganizationPageView(request) :
    return HttpResponse('Search Organization View')

def displayOrganizationPageView(request) :
    return HttpResponse('Display Organization View')

def addOrganizationPageView(request) :
    return HttpResponse('Add Organization View')
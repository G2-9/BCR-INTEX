from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'listings/allListings.html')

def displayListingPageView(request) :
    return HttpResponse('Display Listing View')

def createListingPageView(request) :
    return HttpResponse('Create a listing')
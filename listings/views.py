from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    context = {
        'list' : [1,2,3,4,5]
    }
    return render(request, 'listings/allListings.html', context)

def displayListingPageView(request) :
    return HttpResponse('Display Listing View')

def createListingPageView(request) :
    return HttpResponse('Create a listing')
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.
def indexPageView(request) :
    listing_data = Listing.objects.all()     
    
    context = {
        'listing_data' : listing_data
    }
    return render(request, 'listings/allListings.html', context)

def displayDetailsPageView(request) :
    listing_data = Listing.objects.all()     
    
    context = {
        'listing_data' : listing_data
    }
    return render(request, 'listings/listingdetails.html', context)

def createListingPageView(request) :
    return HttpResponse('Create a listing')
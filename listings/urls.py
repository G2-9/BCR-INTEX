from django.urls import path
from .views import indexPageView, createListingPageView, displayDetailsPageView

urlpatterns = [
    path('listingDetails/', displayDetailsPageView, name='listing_details'),
    path('createListing/', createListingPageView, name='create_listing'),
    path("", indexPageView, name="listings_index")    
]    
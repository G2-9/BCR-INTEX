from django.urls import path
from .views import indexPageView, createListingPageView, displayListingPageView

urlpatterns = [
    path('displayListing/', displayListingPageView, name='display_listing'),
    path('createListing/', createListingPageView, name='create_listing'),
    path("", indexPageView, name="listings_index")    
]    
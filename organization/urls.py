from django.urls import path
from .views import indexPageView, searchOrganizationPageView, displayOrganizationPageView, addOrganizationPageView, registerOrganizationPageView, postListingPageView

urlpatterns = [
    path('postListing/', postListingPageView, name='post_listing'),
    path('registerOrganization/', registerOrganizationPageView, name='register_organization'),
    path('searchOrganization/', searchOrganizationPageView, name='search_organization'),
    path('displayOrganization/', displayOrganizationPageView, name='display_organization'),
    path('addOrganization/', addOrganizationPageView, name='add_organization'),
    path("", indexPageView, name="organization_index") 
]    
from django.urls import path
from .views import indexPageView, searchOrganizationPageView, deleteOrganizationPageView, removeOrganizationPageView, displayOrganizationPageView, addOrganizationPageView, registerOrganizationPageView, postListingPageView, addListingPageView

urlpatterns = [
    path('removeOrganization/', removeOrganizationPageView, name='remove_organization'),
    path('deleteOrganization/', deleteOrganizationPageView, name='delete_organization'),
    path('viewListing/', addListingPageView, name='view_listing'),
    path('postListing/', postListingPageView, name='post_listing'),
    path('registerOrganization/', registerOrganizationPageView, name='register_organization'),
    path('searchOrganization/', searchOrganizationPageView, name='search_organization'),
    path('displayOrganization/', displayOrganizationPageView, name='display_organization'),
    path('addOrganization/', addOrganizationPageView, name='add_organization'),
    path("", indexPageView, name="organization_index") 
]    
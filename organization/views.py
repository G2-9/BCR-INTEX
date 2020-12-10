from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random
from organization.models import Organization
from listings.models import Listing

# Create your views here.
def indexPageView(request) :
    return render(request, 'organization/index.html')

def searchOrganizationPageView(request) :
    return HttpResponse('Search Organization View')

def displayOrganizationPageView(request) :
    return HttpResponse('Display Organization View')

def addOrganizationPageView(request) :
    if request.method == 'POST' :

        new_organization = Organization()

        new_organization.company_name = request.POST.get('company_name')
        new_organization.email = request.POST.get('company_email')
        new_organization.address = request.POST.get('company_streetadd')
        new_organization.organization_id = random.randint(210,10000)
        
        new_organization.save()

        organization_data = Organization.objects.all()

        context = {
            'all_organizations' : organization_data,
            'new_organization' : new_organization
        }
        return render(request, 'organization/vieworganization.html', context)
    else :
        return HttpResponse("NOT FOUND")

def registerOrganizationPageView(request) :
    return render(request, 'organization/orgregister.html')

def postListingPageView(request) :
    return render(request, 'organization/postlisting.html')

def addListingPageView(request) :
    if request.method == 'POST' :

        new_listing = Listing()

        new_listing.job_title = request.POST.get('job_title')
        new_listing.contracts = request.POST.get('contract_length')
        new_listing.city = request.POST.get('city')
        new_listing.compensation = request.POST.get('compensation')
        new_listing.company_website = request.POST.get('company_website')
        new_listing.listing_id = (random.randint(209,10000))   # had to manually input an id FIX ME: AUTOFILL PK

        new_listing.save()

        listing_data = Listing.objects.all()

        context = {
            'all_listings' : listing_data,
            'new_listing' : new_listing
        }
        return render(request, 'organization/viewlisting.html', context)
    else :
        return HttpResponse("NOT FOUND")

def deleteOrganizationPageView(request) :
    return render(request, 'organization/deleteorganization.html')

def removeOrganizationPageView(request) :
    organization = Organization.objects.get(company_name=request.POST['company_name'], email=request.POST['company_email'])
    organization.delete()

    return HttpResponseRedirect("/organization/")

def updateOrganizationPageView(request) :
    return render(request, 'organization/updateorganization.html')

def alterOrganizationPageView(request) :
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        company_email = request.POST.get('company_email')
        new_company_name = request.POST.get('new_company_name')
        new_company_email = request.POST.get('new_company_email')

        organization = Organization.objects.get(company_name=company_name, email=company_email)
        organization.company_name = new_company_name
        organization.email = new_company_email

        organization.save()
        
        return HttpResponseRedirect("/organization/")
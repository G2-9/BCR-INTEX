from django.shortcuts import render
from django.http import HttpResponse
import random
from organization.models import Organization

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
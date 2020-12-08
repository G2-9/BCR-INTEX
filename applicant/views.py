from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'applicant/newindex.html')

def registerPageView(request) :
    return render(request, 'applicant/register.html')

def searchApplicantPageView(request) :
    return HttpResponse('Search Applicant View')

def displayApplicantPageView(request) :
    return HttpResponse('Display Applicant View')

def addApplicantPageView(request) :
    return HttpResponse('Add Applicant View')
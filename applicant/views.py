from django.shortcuts import render
from django.http import HttpResponse
import random
from applicant.models import Applicant

# Create your views here.
def indexPageView(request) :
    return render(request, 'applicant/newindex.html')

def registerPageView(request) :
    return render(request, 'applicant/register.html')

def deleteApplicantPageView(request) :
    return render(request, 'applicant/deleteapplicant.html')

def searchApplicantsPageView(request) :
    return render(request, 'applicant/searchapplicant.html')

def removeApplicantPageView(request) :
    applicant = Applicant.objects.get(first_name=request.GET['first_name'], last_name=request.GET['last_name'], username=request.GET['username'])
    applicant.delete()
    

def displayApplicantPageView(request) :
    return HttpResponse('Display Applicant View')

def addApplicantPageView(request) :
    if request.method == 'POST' :

        new_applicant = Applicant()

        new_applicant.first_name = request.POST.get('first_name')
        new_applicant.last_name = request.POST.get('last_name')
        new_applicant.username = request.POST.get('username')
        new_applicant.email = request.POST.get('email')
        new_applicant.applicant_id = (random.randint(209,10000))   # had to input an applicant_id FIX ME: AUTOFILL PK

        new_applicant.save()

        applicant_data = Applicant.objects.all()

        context = {
            'all_applicants' : applicant_data,
            'new_applicant' : new_applicant
        }
        return render(request, 'applicant/viewapplicant.html', context)
    else :
        return HttpResponse("NOT FOUND")
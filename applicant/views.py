from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random
from applicant.models import Applicant

# Create your views here.
def indexPageView(request) :
    return render(request, 'applicant/newindex.html')

def registerPageView(request) :
    return render(request, 'applicant/register.html')

def deleteApplicantPageView(request) :
    return render(request, 'applicant/deleteapplicant.html')

def updateApplicantsPageView(request) :
    return render(request, 'applicant/updateapplicant.html')

def alterApplicantPageView(request) :
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        username = request.POST.get('username')
        new_firstName = request.POST.get('new_first_name')
        new_lastName = request.POST.get('new_last_name')
        new_username = request.POST.get('new_username')

        applicant = Applicant.objects.get(first_name=firstName, last_name=lastName, username=username)
        applicant.first_name = new_firstName
        applicant.last_name = new_lastName
        applicant.username = new_username

        applicant.save()
        
        return HttpResponseRedirect("/applicant/")

def removeApplicantPageView(request) :
    applicant = Applicant.objects.get(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'])
    applicant.delete()

    return HttpResponseRedirect("/applicant/")    

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
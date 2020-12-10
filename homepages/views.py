from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'homepages/home.html')

def aboutUsPageView(request) :
    return render(request, 'homepages/about.html')

def contactUsPageView(request) :
    return render(request, 'homepages/contact.html')
    
def contactUs2PageView(request) :
    return render(request, 'homepages/contact2.html')
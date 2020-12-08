from django.urls import path
from .views import indexPageView, aboutUsPageView, contactUsPageView, contactUs2PageView, aboutUs2PageView

urlpatterns = [
    path('aboutbcr/', aboutUs2PageView, name='about_us2'),
    path('contactbcr/', contactUs2PageView, name='contact_us2'),
    path('contactus/', contactUsPageView, name='contact_us'),
    path('aboutus/', aboutUsPageView, name='about_us'),
    path("", indexPageView, name="homepages_index")    
]    
from django.urls import path
from .views import indexPageView, aboutUsPageView, contactUsPageView, contactUs2PageView

urlpatterns = [
    path('contact/', contactUs2PageView, name='contact_us2'),
    path('contactus/', contactUsPageView, name='contact_us'),
    path('aboutus/', aboutUsPageView, name='about_us'),
    path("", indexPageView, name="homepages_index")    
]    
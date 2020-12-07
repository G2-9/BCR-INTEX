from django.urls import path
from .views import indexPageView, aboutUsPageView, contactUsPageView

urlpatterns = [
    path('contactus/', contactUsPageView, name='contact_us'),
    path('aboutus/', aboutUsPageView, name='about_us'),
    path("", indexPageView, name="homepages_index")    
]    
from django.urls import path
from .views import indexPageView, searchApplicantPageView, displayApplicantPageView, addApplicantPageView

urlpatterns = [
    path('searchApplicant/', searchApplicantPageView, name='search_applicant'),
    path('displayApplicant/', displayApplicantPageView, name='display_applicant'),
    path('addApplicant/', addApplicantPageView, name='add_applicant'),
    path('', indexPageView, name="applicant_index")    
]
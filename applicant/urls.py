from django.urls import path
from .views import indexPageView, deleteApplicantPageView, displayApplicantPageView, removeApplicantPageView, addApplicantPageView, registerPageView

urlpatterns = [
    path('removeApplicant/', removeApplicantPageView, name='remove_applicant'),
    path('registerApplicant/', registerPageView, name='register_applicant'),
    path('deleteApplicant/', deleteApplicantPageView, name='delete_applicant'),
    path('displayApplicant/', displayApplicantPageView, name='display_applicant'),
    path('addApplicant/', addApplicantPageView, name='add_applicant'),
    path('', indexPageView, name="applicant_index")    
]
from django.db import models
from applicant.models import Applicant

# Create your models here.
class Organization(models.Model) :
    organization_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    sectors = models.CharField(max_length=50)

    def __str__(self) :
        return (self.company_name)

class Offer(models.Model) :
    offer_id = models.IntegerField(primary_key=True)
    applicant_id = models.ForeignKey("applicant.Applicant", on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100)
    organization_id = models.ForeignKey("Organization", on_delete=models.DO_NOTHING)
    contracts = models.CharField(max_length=50)
    matching_skills = models.IntegerField(default=0)

    def __str__(self) :
        return (self.offer_id + ' - ' + self.job_title)
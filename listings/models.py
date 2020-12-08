from django.db import models

# Create your models here.
class Listing(models.Model) :
    listing_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    organization_id = models.IntegerField
    contracts = models.CharField(max_length=50)
    description = models.CharField(max_length=9000)

    def __str__(self) :
        return (self.job_title + ' - ' + self.city)

class Skill(models.Model) :
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=200)

    def __str__(self) :
        return (self.skill_name)
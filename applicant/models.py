from django.db import models

# Create your models here.
class Applicant(models.Model) :
    applicant_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self) :
        return (self.first_name + ' ' + self.last_name)
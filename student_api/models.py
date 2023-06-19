from django.db import models
from accounts.models import *



class SuggestedSupervisor(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    supervisor=models.ManyToManyField(Supervisor)

    def __str__(self):
        return self.university.name +' has Supervisor'

 
class Suggestions(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone_number=models.CharField(max_length=255, blank=True)
    email=models.CharField(max_length=255,null=True)
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


class GraduatedGroups(models.Model):
     name = models.CharField(max_length=255, blank=True)
     description=models.TextField()
     serial=models.CharField(max_length=255,blank=True)
     supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
     students=models.ManyToManyField(Student)
 
     def __str__(self):
         return self.name
 
 

from django.db import models
from accounts.models import *

class ProjectDetails(models.Model):
    group = models.ForeignKey('ProjectGroup', on_delete=models.CASCADE)
    intro=models.TextField(null=True,blank=True)
    project_defination=models.TextField(null=True,blank=True)
    problems=models.TextField()
    goals=models.TextField()
    obstacles=models.TextField()
    assumptions=models.TextField()
    methodology=models.TextField()
    users_char=models.TextField()
    feasibility_study=models.TextField()
    reqiuerments=models.TextField()
    analysis=models.TextField()

class ProjectGroup(models.Model):
     name = models.CharField(max_length=255, blank=True)
     description=models.TextField()
     serial=models.CharField(max_length=255,blank=True)
     supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
     students=models.ManyToManyField(Student)
 
     def __str__(self):
         return self.name
    #  def save(self, *args, **kwargs):
       
    #    super(ProjectGroup, self).save(*args, **kwargs) # Call the real save() method

class RecommendStudentsSupervisor(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone_number=models.CharField(max_length=255, blank=True)
    email=models.CharField(max_length=255,null=True)
    university=models.ForeignKey(MyUsers,on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

   
class StudentSuperVisorWanted(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=9, blank=True)
    email = models.CharField(max_length=255, blank=True,null=True)
    university = models.CharField(max_length=255, blank=True)
    group = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.name

class RecommendSpervisor(models.Model): 
    university = models.CharField(max_length=255,blank=True,null=True)
    supervisors=models.ManyToManyField(Supervisor)

    def __str__(self) -> str:
        return "RecommendSpervisor" 






class Data(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,blank=True)
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.name

    

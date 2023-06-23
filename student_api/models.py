from django.db import models
from accounts.models import *



class SuggestedSupervisor(models.Model):
    university = models.ForeignKey(MyUsers, on_delete=models.CASCADE,blank=True)
    supervisor=models.ManyToManyField(Supervisor)

    def __str__(self):
        return "user"

 
# class Suggestions(models.Model):
#     name = models.CharField(max_length=255, blank=True)
#     phone_number=models.CharField(max_length=255, blank=True)
#     email=models.CharField(max_length=255,null=True)
#     user = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
#     def __str__(self) -> str:
#         return self.name


class GraduatedGroups(models.Model):
     name = models.CharField(max_length=255, blank=True)
     description=models.TextField()
     serial=models.CharField(max_length=255,blank=True)
     supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
     students=models.ManyToManyField(Student)
 
     def __str__(self):
         return self.name
 

class GraduatedProjectPoints(models.Model):
    group = models.ForeignKey(GraduatedGroups, on_delete=models.CASCADE)
    intro=models.TextField()
    project_defination=models.TextField()
    problems=models.TextField()
    goals=models.TextField()
    goals=models.TextField()
    obstacles=models.TextField()
    assumptions=models.TextField()
    agile=models.TextField()
    users_char=models.TextField()
    feasibility_study=models.TextField()
    reqiuerments=models.TextField()
    analysis=models.TextField()
    

    # the student has to login to get in system if he has an account get to page it has tow options 1 is create graduated project group or 2 is join to exist group by serial the graduated group has a name and description and serial and 1 to 5 students and one supervisor when the student tap create graduated project group he fill all needs and put his name first student in that group and through join the serial add the next student and if this student login again and he has a group he redirect to project management page in this page the can fill what graduated project has like introduction and goals and problems fields or can upload files .the system has three type of users the student which i descripted above the second is supervisor and the third is university , the supervisor login if he has an account he redirect to his page which he can see there his graduated project he supervise   and tap one of them to get the same page project management this students has, where he can follows and put some notes for the project students. the third user is university it logins if ti is correct he redirect to his page that can see the all graduated project groups of the university and see progress and archive them if any one oh them complete . please help me how i can create all models i need for all above in django ?? and thanks for helping me 

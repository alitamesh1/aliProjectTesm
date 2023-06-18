from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class MyUsers(AbstractUser):
    pass
    email=models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=9, blank=True, null=True)
    is_student=models.BooleanField(default=False)
    is_supervisor=models.BooleanField(default=False)
    is_university=models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)



class Student(models.Model):
    user=models.OneToOneField(MyUsers,null=True,blank=True,on_delete=models.CASCADE,verbose_name='مستخدم الطالب')
    name = models.CharField(max_length=255,blank=True, null=True)
    email= models.EmailField(blank=True, max_length=254)
    uid = models.CharField(max_length=255, blank=True, null=True)
    phone_number= models.CharField(max_length=20, blank=True, null=True)
    #has_group=models.BooleanField(default=False)
    university = models.CharField(max_length=255, blank=True, null=True)
    college = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True)    
    


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.pk:
            user = MyUsers()
            user.username = self.uid
            user.first_name = self.name
            user.phone = self.phone_number
            user.is_staff=True
            user.is_student=True
            user.is_supervisor=False
            user.is_university=False
            user.set_password(str(self.password))
            self.user = user  
            user.save()
        else:  # If the object already exists, update the associated user object as well
            self.user.username = self.uid
            self.user.first_name = self.name
            self.user.phone = self.phone_number
            self.user.is_staff=True
            self.user.is_student=True
            self.user.is_supervisor=False
            self.user.is_university=False
            self.user.set_password(str(self.password))
            self.user.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.delete()  # Delete the associated user object as well
        super().delete(*args, **kwargs)


##########################################################################
class Supervisor(models.Model):
    user=models.OneToOneField(MyUsers,null=True,blank=True,on_delete=models.CASCADE,verbose_name='مستخدم المشرف')
    name = models.CharField(max_length=255, blank=True, null=True)
    email= models.CharField(null=True,blank=True, max_length=254)
    phone_number= models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            user = MyUsers()
            user.username = self.name
            user.phone = self.phone_number
            user.email=self.email
            user.is_staff=True
            user.is_student=False
            user.is_supervisor=True
            user.is_university=False
            user.set_password(str(self.password))
            self.user = user  
            user.save()
        else:  # If the object already exists, update the associated user object as well
            self.user.username = self.name
            self.user.phone = self.phone_number
            self.user.email =self.email
            self.user.is_staff=True
            self.user.is_student=False
            self.user.is_supervisor=True
            self.user.is_university=False
            self.user.set_password(str(self.password))
            self.user.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.delete()  # Delete the associated user object as well
        super().delete(*args, **kwargs)



###############################################################################
class University(models.Model):
    user=models.OneToOneField(MyUsers,null=True,blank=True,on_delete=models.CASCADE,verbose_name='مستخدم الجامعة')
    name = models.CharField(max_length=255,blank=True, null=True)
    address=models.TextField(null=True)
    password = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            user = MyUsers()
            user.username = self.name
            user.phone = self.address
            user.is_staff=True
            user.is_student=False
            user.is_supervisor=False
            user.is_university=True
            user.set_password(str(self.password))
            self.user = user  
            user.save()
        else:  # If the object already exists, update the associated user object as well
            self.user.username = self.name
            self.user.phone = self.address
            self.user.is_staff=True
            self.user.is_student=False
            self.user.is_supervisor=False
            self.user.is_university=True
            self.user.set_password(str(self.password))
            self.user.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.delete()  # Delete the associated user object as well
        super().delete(*args, **kwargs)



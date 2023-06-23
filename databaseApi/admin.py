from django.contrib import admin
from django.contrib.auth.models import User
from .models import Data
from django.contrib import admin
from .models import *

class ProjectDetailsInline(admin.StackedInline):
    model = ProjectDetails
    extra = 1

class ProjectGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'supervisor')
    inlines = [ProjectDetailsInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        ProjectDetails.objects.create(group=obj)

admin.site.register(ProjectGroup, ProjectGroupAdmin)
admin.site.register(StudentSuperVisorWanted)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'username','user')
    fields = ('name', 'username','user')

    def save_model(self, request, obj, form, change):
        print('save_model called')
        obj.username = request.user.username
        obj.user=request.user
        obj.save()
    # def get_form(self, request, obj=None, **kwargs):
    #     if not request.user.is_superuser and not obj:
    #         self.fields = ('name',)
    #     return super().get_form(request, obj, **kwargs)

admin.site.register(Data, DataAdmin)
admin.site.register(ProjectDetails)

class RecommendStudentsSupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number','email','university','student')
    fields = ('name', 'phone_number','email','university','student')

    def save_model(self, request, obj, form, change):
        print('save_model called')
        obj.university = request.user
        obj.save()
    # def get_form(self, request, obj=None, **kwargs):
    #     if not request.user.is_superuser and not obj:
    #         self.fields = ('name',)
    #     return super().get_form(request, obj, **kwargs)

admin.site.register(RecommendStudentsSupervisor, RecommendStudentsSupervisorAdmin)



class RecommendSpervisorAdmin(admin.ModelAdmin):
    # list_display = ('university', 'supervisor')
    # fields = ('university', 'supervisor')
    list_display = ('university', 'supervisors_names')

    def supervisors_names(self, obj):
        return ", ".join([supervisors.name for supervisors in obj.supervisors.all()])
    supervisors_names.short_description = 'Supervisors'

    def save_model(self, request, obj, form, change):
        print('save_model called')
        obj.university = request.user.username
        obj.save()
    # def get_form(self, request, obj=None, **kwargs):
    #     if not request.user.is_superuser and not obj:
    #         self.fields = ('name',)
    #     return super().get_form(request, obj, **kwargs)

admin.site.register(RecommendSpervisor, RecommendSpervisorAdmin)

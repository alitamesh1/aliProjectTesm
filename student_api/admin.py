from django.contrib import admin
from .models import *
from accounts.models import *

class DataAdmin(admin.ModelAdmin):
    # list_display = ('university', 'supervisor')
    # fields = ('university', 'supervisor')

    def save_model(self, request, obj, form, change):
        print('save_model called')
        obj.university = request.user
        obj.save()
    # def get_form(self, request, obj=None, **kwargs):
    #     if not request.user.is_superuser and not obj:
    #         self.fields = ('name',)
    #     return super().get_form(request, obj, **kwargs)

admin.site.register(SuggestedSupervisor, DataAdmin)
admin.site.register(GraduatedGroups)
admin.site.register(Suggestions)
admin.site.register(GraduatedProjectPoints)

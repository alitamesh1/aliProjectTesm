from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        for user in qs:
            user.username = user.get_username()
        return qs

admin.site.register(MyUsers, CustomUserAdmin)

admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(University)

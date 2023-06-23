from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.authtoken import views as auth_views

urlpatterns=[
    path('token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
    path('data/', GetUser.as_view(), name='user-data'),
    
]

# class UserAdmin(admin.ModelAdmin):
#     exclude = ('password',)

#     def has_add_permission(self, request):
#         return request.user.has_perm('auth.add_user')

#     def has_change_permission(self, request, obj=None):
#         return request.user.has_perm('auth.change_user')

#     def has_delete_permission(self, request, obj=None):
#         return request.user.has_perm('auth.delete_user')

# admin.site.register(User, UserAdmin)
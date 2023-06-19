from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'graduatedgroups', GraduatedGroupsViewSet)
urlpatterns=[
     path('', include(router.urls)),
     path('graduatedgroups/<int:graduated_group_id>/students/', GraduatedGroupsStudentList.as_view()),
    #  path('suggested_supervisor/', SuggestedSupervisorLists.as_view()),
     path('suggested_supervisors/<int:university_id>/', SuggestedSupervisorList.as_view(), name='suggested-supervisor-list'),
    #  path('group_project/', GraduatedGroupsList.as_view(), name='group_projectlist'),
    #  path('group_project/<int:pk>/', GraduatedGroupDetails.as_view(), name='group_projectDetails'),
] 





from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers
from .views import RecommendSpervisorViewSet,RecommendSpervisorUniversityList
urlpatterns=[
    path('re/',RecommendSpervisorViewSet.as_view()),
    path('project-details/', ProjectDetailsList.as_view(), name='project-details-list'),
    path('project-details/<int:pk>/', ProjectDetailsDetail.as_view(), name='project-details-detail'),
    path('project-group/', ProjectGroupList.as_view(), name='project-group-list'),
    path('project-group-serial/<str:serial>', GroupProjectSerialList.as_view(), name='project-group-list'),
    path('project-group/<int:pk>/', ProjectGroupDetail.as_view(), name='project-group-detail'),
    path('recommend-spervisor/', RecommendSpervisorListView.as_view(), name='recommend-spervisor-list'),
    path('recommend-spervisor/<int:pk>/', RecommendSpervisorDetailView.as_view(), name='recommend-spervisor-detail'),   
    path('student-wanted-spervisor/', StudentSuperVisorWantedList.as_view(), name='wantList'),   
    path('student-wanted-spervisor/<int:pk>/', StudentSuperVisorWantedDetail.as_view(), name='wantDetails'), 
    path('recommendspervisor/', RecommendSpervisorListAPIView.as_view(), name='recommendspervisor-list'),  
    path('recommendspervisor/<str:university>/', RecommendSpervisorUniversityList.as_view(), name='recommendspervisorIniversity-list'),  
]
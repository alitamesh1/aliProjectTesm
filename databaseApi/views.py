from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics,status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import RecommendSpervisor
from rest_framework.response import Response
from .serializers import *

class RecommendSpervisorViewSet(generics.ListCreateAPIView):
    queryset = RecommendSpervisor.objects.all()
    serializer_class = RecommendSpervisorSerializer




class ProjectDetailsList(generics.ListCreateAPIView):
    queryset = ProjectDetails.objects.all()
    serializer_class = ProjectDetailsSerializer

class ProjectDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectDetails.objects.all()
    serializer_class = ProjectDetailsSerializer

class ProjectGroupList(generics.ListCreateAPIView):
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
    def perform_create(self, serializer):
        # Create the new ProjectGroup instance
        group = serializer.save()

        # Create a new ProjectDetails instance for the new ProjectGroup
        project_details = ProjectDetails.objects.create(group=group)

        # Serialize the new ProjectDetails instance
        project_details_serializer = ProjectDetailsSerializer(project_details)

        # Add the serialized ProjectDetails instance to the response data
        serializer.data['project_details'] = project_details_serializer.data
class RecommendSpervisorUniversityList(generics.ListAPIView):
    serializer_class = RecommendSpervisorApiSerializer

    def get_queryset(self):
        #graduated_group_id = self.kwargs['graduated_group_id']
        university=self.kwargs['university']
        #return RecommendSpervisor.objects.get(id=graduated_group_id).university.all()
        return RecommendSpervisor.objects.filter(university=university)
    
class ProjectGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update the project details for the updated project group
        project_details = ProjectDetails.objects.get(group=instance)
        project_details_serializer = ProjectDetailsSerializer(project_details, data=request.data)
        project_details_serializer.is_valid(raise_exception=True)
        project_details_serializer.save()

        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        project_details = ProjectDetails.objects.get(group=instance)
        project_details.delete()

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
    



    ##########


class RecommendSpervisorListView(APIView):
    def get(self, request, format=None):
        recommend_spervisors = RecommendSpervisor.objects.all()
        serializer = RecommendSpervisorSerializer(recommend_spervisors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecommendSpervisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecommendSpervisorDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(RecommendSpervisor, pk=pk)

    def get(self, request, pk, format=None):
        recommend_spervisor = self.get_object(pk)
        serializer = RecommendSpervisorSerializer(recommend_spervisor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recommend_spervisor = self.get_object(pk)
        serializer = RecommendSpervisorSerializer(recommend_spervisor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recommend_spervisor = self.get_object(pk)
        recommend_spervisor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StudentSuperVisorWantedList(generics.ListCreateAPIView):
    queryset = StudentSuperVisorWanted.objects.all()
    serializer_class = StudentSuperVisorWantedSerializer


class StudentSuperVisorWantedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSuperVisorWanted.objects.all()
    serializer_class = StudentSuperVisorWantedSerializer

class RecommendSpervisorListAPIView(generics.ListAPIView):
    serializer_class = RecommendSpervisorApiSerializer
    
    queryset = RecommendSpervisor.objects.all()

class RecommendSpervisorUniversityList(generics.ListAPIView):
    serializer_class = RecommendSpervisorApiSerializer

    def get_queryset(self):
        #graduated_group_id = self.kwargs['graduated_group_id']
        university=self.kwargs['university']
        #return RecommendSpervisor.objects.get(id=graduated_group_id).university.all()
        return RecommendSpervisor.objects.filter(university=university)
    
    
class GroupProjectSerialList(generics.ListAPIView):
    serializer_class = ProjectGroupSerializer

    def get_queryset(self):
        #graduated_group_id = self.kwargs['graduated_group_id']
        serial=self.kwargs['serial']
        #return RecommendSpervisor.objects.get(id=graduated_group_id).university.all()
        return ProjectGroup.objects.filter(serial=serial)
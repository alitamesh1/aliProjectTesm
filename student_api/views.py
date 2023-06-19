from django.shortcuts import render
from .serializers import *
from rest_framework import generics,status,viewsets
from rest_framework.response import Response

# Create your views here.

class SuggestedSupervisorLists(generics.ListCreateAPIView):
    serializer_class = SuggestedSupervisorSerializer

    def get_queryset(self):
        queryset = SuggestedSupervisor.objects.all()
        university_id = self.request.query_params.get('university_id', None)
        if university_id is not None:
            queryset = queryset.filter(university_id=university_id)
        return queryset
    
  
class GraduatedGroupsViewSet(viewsets.ModelViewSet):
    queryset = GraduatedGroups.objects.all()
    serializer_class = GraduatedGroupsWERSerializer

class SuggestedSupervisorList(generics.ListCreateAPIView):
    serializer_class = SuggestedSupervisorSerializer

    def get_queryset(self):
        university_id = self.kwargs['university_id']
        return SuggestedSupervisor.objects.filter(university_id=university_id)

# class GraduatedGroupsList(generics.ListCreateAPIView):
#     queryset=GraduatedGroups.objects.all()
#     serializer_class=GraduatedProjectSerializer
#     def get(self,request):
#         groups=GraduatedGroups.objects.all()
#         serializers=GraduatedProjectSerializer(groups,many=True)
#         return Response(serializers.data)
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data, context=self.get_serializer_context())
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
# class GraduatedGroupDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset=GraduatedGroups.objects.all()
#     serializer_class=GraduatedProjectSerializer

# class GraduatedGroupsList(generics.ListCreateAPIView):
#     queryset = GraduatedGroups.objects.all()
#     serializer_class = GraduatedProjectSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data, context=self.get_serializer_context())
#         serializer.is_valid(raise_exception=True)
#         instance = serializer.save()

#         # Create new students
#         students_data = request.data.get('students', [])
#         for student_data in students_data:
#             student_fields = student_data.pop('student')
#             student = Student.objects.create(**student_fields)
#             GroupMembership.objects.create(student=student, group=instance, **student_data)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#     def perform_create(self, serializer):
#         serializer.save()

# class GraduatedGroupDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = GraduatedGroups.objects.all()
#     serializer_class = GraduatedProjectSerializer
from rest_framework import serializers,generics
from .models import *
from accounts.models import *

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['id', 'name', 'email','phone_number','major']

class SuggestedSupervisorSerializer(serializers.ModelSerializer):
    supervisor = SupervisorSerializer(many=True)

    class Meta:
        model = SuggestedSupervisor
        fields = ['id', 'university', 'supervisor']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','email','uid','phone_number','university','college','major']

# class GraduatedProjectSerializer(serializers.ModelSerializer):
#     students=StudentSerializer(many=True)
#     class Meta:
#         model=GraduatedGroups
#         fields='__all__'

#         def create(self, validated_data):
#             students_data = validated_data.pop('students', [])
#             instance = super().create(validated_data)
#             for student_data in students_data:
#              student = Student.objects.create(group=instance, **student_data)
#             instance.students.add(student)
#             return instance

class GraduatedGroupsStudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        graduated_group_id = self.kwargs['graduated_group_id']
        return GraduatedGroups.objects.get(id=graduated_group_id).students.all()

class GraduatedGroupsWERSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    #students = StudentSerializer(many=True,write_only=True)

    class Meta:
        model = GraduatedGroups
        fields = ['id', 'name', 'description', 'serial', 'supervisor', 'students']



class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ('id', 'username', 'email')

class SuggestionsSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Suggestions
        fields = ('id', 'name', 'phone_number', 'email', 'user')



class GraduatedGroupsProSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduatedGroups
        fields = '__all__'

class GraduatedProjectPointsSerializer(serializers.ModelSerializer):
    group=GraduatedGroupsProSerializer()
    class Meta:
        model = GraduatedProjectPoints
        fields = '__all__'

# class GroupMembershipSerializer(serializers.ModelSerializer):
#     student=StudentSerializer(many=True)
#     class Meta:
#         model = GroupMembership
#         fields = '__all__'

# class GraduatedProjectSerializer(serializers.ModelSerializer):
#     student = GroupMembershipSerializer(many=True, required=False)

#     class Meta:
#         model = GraduatedGroups
#         fields = '__all__'

#     def create(self, validated_data):
#         students_data = validated_data.pop('students', [])
#         instance = super().create(validated_data)
#         for student_data in students_data:
#             student = Student.objects.create(group=instance, **student_data)
#             instance.students.add(student)
#         return instance

#     def update(self, instance, validated_data):
#         students_data = validated_data.pop('students', [])
#         instance = super().update(instance, validated_data)
#         # Remove existing students that are not in the updated data
#         existing_students = instance.students.all()
#         for student in existing_students:
#             student_data = next((item for item in students_data if item.get('id') == student.id), None)
#             if not student_data:
#                 student.delete()
#         # Add or update students that are in the updated data
#         for student_data in students_data:
#             if 'id' in student_data:  # Update existing student
#                 student = Student.objects.get(id=student_data['id'])
#                 for key, value in student_data.items():
#                     setattr(student, key, value)
#                 student.save()
#             else:  # Create new student
#                 student = Student.objects.create(group=instance, **student_data)
#                 instance.students.add(student)
#         return instance
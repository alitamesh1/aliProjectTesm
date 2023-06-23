# serializers.py
from rest_framework import serializers
from .models import RecommendSpervisor,StudentSuperVisorWanted
from accounts.models import *

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'

class RecommendSpervisorSerializer(serializers.ModelSerializer):
    supervisors = SupervisorSerializer(many=True)

    class Meta:
        model = RecommendSpervisor
        fields = '__all__'

    def create(self, validated_data):
        supervisors_data = validated_data.pop('supervisors')
        recommend_spervisor = RecommendSpervisor.objects.create(**validated_data)
        for supervisor_data in supervisors_data:
            supervisor = Supervisor.objects.get(pk=supervisor_data['id'])
            recommend_spervisor.supervisors.add(supervisor)
        return recommend_spervisor

    def update(self, instance, validated_data):
        supervisors_data = validated_data.pop('supervisors', None)
        instance.university = validated_data.get('university', instance.university)
        instance.save()
        if supervisors_data is not None:
            instance.supervisors.clear()
            for supervisor_data in supervisors_data:
                supervisor = Supervisor.objects.get(pk=supervisor_data['id'])
                instance.supervisors.add(supervisor)
        return instance
    

    ############
from rest_framework import serializers
from .models import ProjectDetails, ProjectGroup,StudentSuperVisorWanted

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails
        fields = '__all__'

class ProjectGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGroup
        fields = '__all__'

# class ProjectGroupwantedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectGroup
#         fields = '__all__'

class StudentSuperVisorWantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSuperVisorWanted
        fields = '__all__'
class supervisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['id', 'name','email','phone_number']
class RecommendSpervisorApiSerializer(serializers.ModelSerializer):
    supervisors=supervisorsSerializer(many=True)
    class Meta:
        model = RecommendSpervisor
        fields = ['id', 'university', 'supervisors']
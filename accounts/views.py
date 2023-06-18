from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class GetUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        content = {
            'id':user.id,
            'username': user.username,
            'phone': user.phone,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_superuser':user.is_superuser,
            'is_staff':user.is_staff,
            'is_active':user.is_active,
            'is_student':user.is_student,
            'is_supervisor':user.is_supervisor,
            'is_university':user.is_university
            

        }
        return Response(content)


def redirect_to_admin(request):
    return HttpResponseRedirect(reverse("admin:login"))

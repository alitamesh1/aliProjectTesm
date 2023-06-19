
from django.contrib import admin
from django.urls import path,include
from accounts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", redirect_to_admin, name="to_admin"),
    path('user/', include('accounts.urls')),
    path('student/', include('student_api.urls')),

]

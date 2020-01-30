"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from name_check import views
from present import views as views_present
from manage_student import views as view_student


urlpatterns = [
    #name_check
    path('admin/', admin.site.urls),
    path('login/', views.inclass), 
    path('course/<int:course_id>', views.course),
    path('qrcode', views.qrcode),

    #present
    path('dashboard/', views_present.showstudent),
    path('search/<int:no_attend>', views_present.search),

    path('', view_student.index),
    path('addstudent', view_student.add_student),
    path('editstudent/<int:id>', view_student.edit_student),
    path('subject', view_student.subject),
    path('addsubject', view_student.add_subject),
    path('editsubject/<int:id>', view_student.edit_subject)
]

"""classroom_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from src.pages.views import home_view, home_class_view, home_student_view, home_assign_view, add_class_view, show_class_view, add_student_view, show_student_view, add_assign_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('homeClass/', home_class_view),
    path('homeStudent/', home_student_view),
    path('homeAssign/', home_assign_view),
    path('addClass/', add_class_view),
    path('showClass/', show_class_view),
    path('addStudent/', add_student_view),
    path('showStudent/', show_student_view),
    path('addToClass/', add_assign_view),
]

"""
URL configuration for Online_Exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Online_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name='Index'),
    path('reg/',views.Register,name='Register'),
    path('log/',views.Login,name='Login'),
    path('view/',views.View,name='View'),
    path('student/',views.Student,name='Student'),
    path('profile/',views.Profile,name='Profile'),
]

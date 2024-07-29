"""
URL configuration for Zero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Zero import views # This must be imported manualy won't the givven by defulat, it just imports views.py (Which must be created manually)

urlpatterns = [
    path('admin/', admin.site.urls), # this would be /admin page 
    path('', views.index, name='index'), # This function tell's to run the the index function of the view.py amd the empty string '' tells to run it by defulat
    path('about/', views.about, name='about'), # this would be /adbout page 
    path('services/', views.services, name='services'), # this would redirect to /services pages 
]

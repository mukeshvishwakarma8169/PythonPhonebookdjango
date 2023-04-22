"""phonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from phonebookapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.phonemasterindex, name='phone'),
    path('phone', views.phonemasterindex, name='phone'),
    path('phoneaddnew', views.phonemasteraddnew, name='phoneaddnew'),
    path('phonemasteredit/<int:id>', views.phonemasteredit, name='phonemasteredit'),
    path('phoneupdate', views.phonemasterupdate, name='phoneupdate'),
    path('phonedelete/<int:id>', views.phonemasterdestroy, name='phonedelete'),
]

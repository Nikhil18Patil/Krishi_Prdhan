"""
URL configuration for Krishi_Prdhan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Krishi_Prdhan.views import home
from Krishi_Prdhan.views import contact
from Krishi_Prdhan.views import product
from Krishi_Prdhan.views import service
from Krishi_Prdhan.views import about
from Krishi_Prdhan.views import newss
from Krishi_Prdhan.views import success
from Krishi_Prdhan.views import goverment
from Krishi_Prdhan.views import crop
from Krishi_Prdhan.views import community
from Krishi_Prdhan.views import whether
from Krishi_Prdhan.views import marketinfo
from Krishi_Prdhan.views import training
from Krishi_Prdhan.views import expert
from Krishi_Prdhan.views import blogone
from Krishi_Prdhan.views import blogtwo
from Krishi_Prdhan.views import newnews
from Krishi_Prdhan.views import newdetail
from Krishi_Prdhan.views import crop_form
from Krishi_Prdhan.views import solution
from .views import register, login, logout_view

urlpatterns = [
    path('register/',register, name="register" ),
    path('login/', login, name="login"),
    path('logout', logout_view, name="logout"),
    path('', home,name="home"),
    path('contact/', contact,name="contact"),
    path('product/',product,name="product"),
    path('service/',service, name="service"),
    path('admin/', admin.site.urls),
    path('about/',about, name="about"),
    path('news/', newss, name="news"),
    path('success/',success,name="success"),
    path('goverment', goverment,name="goverment"),
    path('crop',crop_form,name="crop"),
    path('community',community,name="community"),
    path('weather',whether,name="weather"),
    path('marketinfo',marketinfo,name="marketinfo"),
    path('training',training,name="training"),
    path('expert',expert,name="expert"),
    path('blogone/',blogone,name="blogone"),
    path('blogtwo/',blogtwo,name="blogtwo"),
    path('newnews/',newnews,name="newnews"),
    path('new/<id>',newdetail,name="new"),
    path('solution/',solution,name="solution"),
    path('crop_form/',crop_form,name="cropform"),



  
]


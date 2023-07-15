from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from data.models import contactus
from data.models import emails
from mydata.models import mynews
from data.models import Cropdetail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Krishi_Prdhan.serializations import serializations
import json
import requests
from data.models import news


@csrf_exempt
def home(request):
    if request.method=="POST":
        Email=request.POST.get('Email')
        ea=emails(Email=Email)
        ea.save()
    template= loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def contact(request):
    if request.method=="POST":
      if 'send' in request.POST:  
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Subject=request.POST.get('Subject')
        Message=request.POST.get('Message')
        da=contactus(Name=Name,Email=Email,Subject=Subject,Message=Message)
        da.save()
      if 'Email' in request.POST:
        Email=request.POST.get('Email')
        ea=emails(Email=Email)
        ea.save()  
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())

def product(request):
    template=loader.get_template('product.html')
    return HttpResponse(template.render())

def service(request):
    template=loader.get_template('service.html')
    return HttpResponse(template.render())

def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render()) 

def newss(request):
    nil=news.objects.all() 
    context={
          'news':nil  
    } 
    return render(request,'news.html',context) 
     

def success(request):
    template=loader.get_template('blog.html')
    return HttpResponse(template.render()) 


def community(request):
    template=loader.get_template('community.html')
    return HttpResponse(template.render())  

def goverment(request):
    template=loader.get_template('goverment.html')
    return HttpResponse(template.render())   

def crop(request):
    template=loader.get_template('Crop.html')
    return HttpResponse(template.render())

def whether(request):
    template=loader.get_template('Weather.html')
    return HttpResponse(template.render())

def marketinfo(request):
    template=loader.get_template('MarketInformation.html')
    return HttpResponse(template.render())

def training(request):
    template=loader.get_template('Traning.html')
    return HttpResponse(template.render())

def expert(request):
    template=loader.get_template('expert.html')
    return HttpResponse(template.render())  

def blogone(request):
    template=loader.get_template('detail_1.html')
    return HttpResponse(template.render())

def blogtwo(request):
    template=loader.get_template('detail_2.html')
    return HttpResponse(template.render())  

@api_view(['GET'])
def newnews(request):
   if request.method=="GET":
        result=mynews.objects.all().using('itsnews')
        serialize=serializations(result,many=True)  
   return Response(serialize.data) 

def newdetail(request,id):
     result=news.objects.get(id=id)
     data={
          'news':result
     }
     return render(request,'news_d1.html',data)

@csrf_exempt
def crop_form(request):
    if request.method=="POST":

        name=request.POST.get('crop-name')
        type=request.POST.get('crop-type')
        area=request.POST.get('crop-area')
        season=request.POST.get('crop-season')
        data=Cropdetail(name=name, type=type,area=area,season=season)
        data.save()
    template =loader.get_template('Crop.html')
   
    
    return HttpResponse(template.render())

def solution(request):
    
            form =Cropdetail.objects.all().last()
        
           
           
            
            
            return render(request, 'solution.html', {'name':form})
   
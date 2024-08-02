
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
from mydata.models import UserProfile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        # Check if the username is already taken
        if UserProfile.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})

        # Create a new user with a hashed password
        new_user = UserProfile(username=username, password=make_password(password))
        new_user.save()
        return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return render(request, 'login.html', {'error': 'Username does not exist.'})

        # Verify the password using check_password
        if check_password(password, user.password):
            # Store user data in the session
            request.session['user'] = {'username': username}
            return redirect('home')  # Redirect to the home page upon successful login

        return render(request, 'login.html', {'error': 'Incorrect password.'})

    return render(request, 'login.html')


def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('login')
















@csrf_exempt
def home(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       if request.method=="POST":
           Email=request.POST.get('Email')
           ea=emails(Email=Email)
           ea.save()
       
       
       return render(request, 'index.html', {'c':current_user})
    else:
        return redirect('login')


@csrf_exempt
def contact(request):

  if 'user' in request.session:
    current_user = request.session['user']   
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
  else:
        return redirect('login')
    

def product(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       itemplate=loader.get_template('product.html')
       return HttpResponse(template.render())
    else:
        return redirect('login')
    

def service(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       template=loader.get_template('service.html')
       return HttpResponse(template.render())
    else:
        return redirect('login')
    

def about(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       template=loader.get_template('about.html')
       return HttpResponse(template.render()) 
    else:
        return redirect('login')
    

def newss(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       nil=news.objects.all() 
       context={
          'news':nil  
       } 
       return render(request,'news.html',context) 
    else:
        return redirect('login')
    
     

def success(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       template=loader.get_template('blog.html')
       return HttpResponse(template.render()) 
    else:
        return redirect('login')
    


def community(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       template=loader.get_template('community.html')
       return HttpResponse(template.render())  
    else:
        return redirect('login')
    
def goverment(request):
    if 'user' in request.session:
       current_user = request.session['user']   
       template=loader.get_template('goverment.html')
       return HttpResponse(template.render())   
    else:
        return redirect('login')
    

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
   
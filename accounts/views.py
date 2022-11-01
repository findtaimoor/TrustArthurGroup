from ast import Global, Or
from calendar import month
from copy import error
from ctypes import Union
from datetime import date,time,datetime
import datetime
import email
from email import header
from functools import total_ordering
from http.client import responses
from operator import and_
from pickle import FALSE
from unicodedata import name
from urllib import request
from urllib.parse import ParseResult
from urllib.request import Request
from wsgiref.util import request_uri
from django.conf import settings
from django.shortcuts import render,redirect, reverse
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django import utils
import logging
from .generic import *
from dateutil.relativedelta import relativedelta

import uuid
from http import server
import smtplib




# Create your views here.

def validate_username(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
  
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    return JsonResponse(data)

# def validate_user(request):
#     username = request.GET.get('username', None)
#     print(username)
#     data = {
#         'is_taken': User.objects.filter(username=username).exists()
#     }
#     print(data)
#     if data['is_taken']:
#         data['error_message'] = 'A user with this username already exists.'
#     return JsonResponse(data)

import re

def home(request):

    home = HomeInfoSection.objects.all().last()
    banner = HomeBanner.objects.all()
    
    wwd = HomeWhatWeDo.objects.all()
 
    explore = HomeExploreProducts.objects.all()
    testi = HomeTestinomials.objects.all()
    return render(request, 'accounts/index.html',{'home':home,'banner':banner,'wwd':wwd,'explore':explore,'testi':testi})

def about(request):
   try:
    home = HomeInfoSection.objects.all().last()
    about = AboutInfoSection.objects.all().last()
    ccv = AboutCompanyCore.objects.all()
    testi = AboutTestinomials.objects.all()
    members = AboutTeamMembers.objects.all()
    b_members = AboutBoardMembers.objects.all()
    return render(request, 'accounts/about.html',{'home':home,'about':about,'ccv':ccv,'testi':testi,'members':members,'b_members':b_members})
   except:
     return render(request,'accounts/index.html')
def news(request):
    try:
     news = News.objects.all()
     return render(request, 'accounts/news.html',{'news':news})
    except:
        return render(request, 'accounts/index.html')
def editprofiledetails(request):
 
    gender = ['Male','Female']
    if IndividualRegister.objects.filter(user=request.user).exists():
        cuser = IndividualRegister.objects.get(user=request.user)
        if cuser.joint_account == True:
            juser = AnotherJoinAccountRegister.objects.get(individual_user=cuser)
            if request.method == "POST":
                cuser.fullname = request.POST['fullname']
                cuser.phone = request.POST['phone']
                cuser.house_number = request.POST['house_number']
                cuser.street_name = request.POST['street_name']
                cuser.city = request.POST['city']
                cuser.state = request.POST['state']
                cuser.country = request.POST['country']
                cuser.birthdate = request.POST['birthdate']
                cuser.gender = request.POST['gender']
                cuser.occupation = request.POST['occupation']
                cuser.NIN = request.POST['NIN']
                cuser.BVN =   request.POST['BVN']
                individual_signature = request.FILES.get('individual_signature')
                individual_photo = request.FILES.get('individual_photo')

                if individual_signature is not None:
                    cuser.individual_signature = individual_signature
                if individual_photo is not None:
                    cuser.individual_photo = individual_photo

                cuser.kin_name = request.POST['kin_name']
                cuser.kin_relationship = request.POST['kin_relationship']
                cuser.kin_phone = request.POST['kin_phone']
                cuser.kin_house_number = request.POST['kin_house_number']
                cuser.kin_street_name = request.POST['kin_street_name']
                cuser.kin_city = request.POST['kin_city']
                cuser.kin_state = request.POST['kin_state']
                cuser.kin_country = request.POST['kin_country']
                cuser.save()

                juser.another_name = request.POST['another_name']
                juser.another_phone = request.POST['another_phone']
                juser.another_house_number = request.POST['another_house_number']
                juser.another_street_name = request.POST['another_street_name']
                juser.another_city = request.POST['another_city']
                juser.another_state = request.POST['another_state']
                juser.another_country = request.POST['another_country']
                juser.another_birthdate = request.POST['another_birthdate']
                juser.another_gender = request.POST['another_gender']
                juser.another_occupation = request.POST['another_occupation']
                another_signature = request.FILES.get('another_signature')
                another_photo =   request.FILES.get('another_photo')

                if another_signature is not None:
                    juser.another_signature = another_signature
                if another_photo is not None:
                    juser.another_photo = another_photo

                juser.save()
                messages.success(request,'Updated Succesfully.')
                return redirect('editprofiledetails')

            return render(request, 'accounts/editprofiledetails.html',{'cuser':cuser,'juser':juser,'gender':gender})
        else:
            if request.method == "POST":
                cuser.fullname = request.POST['fullname']
                cuser.phone = request.POST['phone']
                cuser.house_number = request.POST['house_number']
                cuser.street_name = request.POST['street_name']
                cuser.city = request.POST['city']
                cuser.state = request.POST['state']
                cuser.country = request.POST['country']
                cuser.birthdate = request.POST['birthdate']
                cuser.gender = request.POST['gender']
                cuser.occupation = request.POST['occupation']
                cuser.NIN = request.POST['NIN']
                cuser.BVN =   request.POST['BVN']
                individual_signature = request.FILES.get('individual_signature')
                individual_photo = request.FILES.get('individual_photo')

                if individual_signature is not None:
                    cuser.individual_signature = individual_signature
                if individual_photo is not None:
                    cuser.individual_photo = individual_photo

                cuser.kin_name = request.POST['kin_name']
                cuser.kin_relationship = request.POST['kin_relationship']
                cuser.kin_phone = request.POST['kin_phone']
                cuser.kin_house_number = request.POST['kin_house_number']
                cuser.kin_street_name = request.POST['kin_street_name']
                cuser.kin_city = request.POST['kin_city']
                cuser.kin_state = request.POST['kin_state']
                cuser.kin_country = request.POST['kin_country']
                cuser.save()
                messages.success(request,'Updated Succesfully.')
                return redirect('editprofiledetails')

            return render(request, 'accounts/editprofiledetails.html',{'cuser':cuser,'gender':gender})

    elif BusinessRegister.objects.filter(user=request.user).exists():
        cuser = BusinessRegister.objects.get(user=request.user)
        if request.method == "POST":
            cuser.company_name = request.POST['company_name']
            cuser.company_number = request.POST['company_number']
            cuser.tax_id = request.POST['tax_id']
            cuser.company_industry = request.POST['company_industry']
            cuser.company_date = request.POST['company_date']
            cuser.NIN = request.POST['NIN']
            cuser.BVN =   request.POST['BVN']
            cuser.phoneno = request.POST['phone']
            cuser.houseno = request.POST['house_number']
            cuser.street_name = request.POST['street_name']
            cuser.city = request.POST['city']
            cuser.state = request.POST['state']
            cuser.country = request.POST['country']
            cuser.em1 = request.POST['name1']
            cuser.em2 = request.POST['name2']
            cuser.em3 = request.POST['name3']
            cuser.em4 = request.POST['name4']
            signature = request.FILES.get('signature')
            photo = request.FILES.get('photo')

            if signature is not None:
                cuser.signature = signature
            if photo is not None:
                cuser.photo = photo

            cuser.save()
            messages.success(request,'Updated Succesfully.')
            return redirect('editprofiledetails')
        return render(request, 'accounts/editprofiledetails.html',{'cuser':cuser})
 

    elif AnotherJoinAccountRegister.objects.filter(user=request.user).exists():
        auser = AnotherJoinAccountRegister.objects.get(user=request.user)
        if request.method == "POST":
            auser.individual_user.fullname = request.POST['fullname']
            auser.individual_user.phone = request.POST['phone']
            auser.individual_user.house_number = request.POST['house_number']
            auser.individual_user.street_name = request.POST['street_name']
            auser.individual_user.city = request.POST['city']
            auser.individual_user.state = request.POST['state']
            auser.individual_user.country = request.POST['country']
            auser.individual_user.birthdate = request.POST['birthdate']
            auser.individual_user.gender = request.POST['gender']
            auser.individual_user.occupation = request.POST['occupation']
            auser.individual_user.NIN = request.POST['NIN']
            auser.individual_user.BVN =   request.POST['BVN']
            individual_signature = request.FILES.get('individual_signature')
            individual_photo = request.FILES.get('individual_photo')

            if individual_signature is not None:
                auser.individual_user.individual_signature = individual_signature
            if individual_photo is not None:
                auser.individual_user.individual_photo = individual_photo

            auser.individual_user.kin_name = request.POST['kin_name']
            auser.individual_user.kin_relationship = request.POST['kin_relationship']
            auser.individual_user.kin_phone = request.POST['kin_phone']
            auser.individual_user.kin_house_number = request.POST['kin_house_number']
            auser.individual_user.kin_street_name = request.POST['kin_street_name']
            auser.individual_user.kin_city = request.POST['kin_city']
            auser.individual_user.kin_state = request.POST['kin_state']
            auser.individual_user.kin_country = request.POST['kin_country']
            auser.individual_user.save()

            auser.another_name = request.POST['another_name']
            auser.another_phone = request.POST['another_phone']
            auser.another_house_number = request.POST['another_house_number']
            auser.another_street_name = request.POST['another_street_name']
            auser.another_city = request.POST['another_city']
            auser.another_state = request.POST['another_state']
            auser.another_country = request.POST['another_country']
            auser.another_birthdate = request.POST['another_birthdate']
            auser.another_gender = request.POST['another_gender']
            auser.another_occupation = request.POST['another_occupation']
            another_signature = request.FILES.get('another_signature')
            another_photo =   request.FILES.get('another_photo')

            if another_signature is not None:
                auser.another_signature = another_signature
            if another_photo is not None:
                auser.another_photo = another_photo

            auser.save()
            messages.success(request,'Updated Succesfully.')
            return redirect('editprofiledetails')

        return render(request, 'accounts/editprofiledetails.html',{'auser':auser,'gender':gender})
 



def orders(request):
   try:
    orders = OrderPlaced.objects.filter(user=request.user)
    # pastorder = OrderPlaced.objects.filter(due_date__lt=utils.timezone.now(),user=request.user)
    # currentorder = OrderPlaced.objects.filter(due_date__gte=utils.timezone.now(),user=request.user)
    # pastordersorted = sorted(pastorder, key=lambda x: x.due_date, reverse=True)
    # currentordersorted = sorted(currentorder, key=lambda x: x.due_date)
    orders = sorted(orders, key=lambda x: x.ordered_date_time, reverse=True)

    

    return render(request, 'accounts/orders.html',{'orders':orders})
   except:
    return render(request,'accounts/index.html')
def customerquote(request):
   
    cq = Quote.objects.filter(user=request.user)
    return render(request, 'accounts/quote.html',{'cq':cq})
   
def customerquotedelete(request,id):
#    try:
    quote = Quote.objects.get(pk=id)
    quote.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('customerquote')
#    except:
#     return render(request,'accounts/index.html')

@csrf_exempt
def signup(request):
#    try:
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        
        typeofuser = request.POST['typeofuser']
        
         
        if typeofuser == 'corporate':
            print('ahmad')

            company_email = request.POST['company_email']
            username = company_email[:company_email.index('@')]
            password = request.POST['pass']
            company_name = request.POST['company_name']
            company_number = request.POST['company_number']
            tax_id = request.POST['tax_id']
            company_industry = request.POST['company_industry']
            company_date = request.POST['company_date']
            NIN = request.POST['NIN']
            BVN =   request.POST['BVN']
            phoneno = request.POST['phone']
            houseno = request.POST['house_number']
            street_name = request.POST['street_name']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            em1 = request.POST['name1']
            em2 = request.POST['name2']
            em3 = request.POST['name3']
            em4 = request.POST['name4']
            signature = request.FILES['signature']
            photo = request.FILES['photo']
            
            userb = User.objects.create_user(username, company_email, password)
            userb.is_active=True



            userb.save()

            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaafarhan')

            BusinessRegister(user = userb,typeofuser=typeofuser,company_name=company_name,company_number=company_number,tax_id=tax_id,
            company_industry=company_industry,company_date=company_date,NIN=NIN,BVN=BVN,phoneno=phoneno,houseno=houseno,
            street_name=street_name,city=city, state=state,country=country, em1=em1,em2=em2,em3=em3, em4=em4, 
            signature=signature,photo=photo).save()
           
            #---Send mail_--
            Send_Email = "trustauthurgroup@gmail.com"
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(Send_Email, 'nxbukvaocrzzetnu')
            mail=server.sendmail


            if company_email:
                
                a="""Your Email registered successfully"""
                
                msg_chapass = "\r\n".join([
                            
                            "Signup",
                            "",
                            a
                            ]) 

                
                mail(Send_Email,company_email,msg_chapass)
                messages.success(request,'Email sent')
                print(mail)
                print('yes')


        
        if typeofuser == 'individual':

            individual_email = request.POST['individual_email']
            username = individual_email[:individual_email.index('@')]
            
            password = request.POST['password']
            f_name = request.POST['fullname']
            l_name = request.POST['fullname']
            phone = request.POST['phone']
            house_number = request.POST['house_number']
            street_name = request.POST['street_name']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            birthdate = request.POST['birthdate']
            gender = request.POST['gender']
            occupation = request.POST['occupation']
            NIN = request.POST['NIN']
            BVN =   request.POST['BVN']
            joint_account = request.POST['joint_account']
            individual_signature = request.FILES['individual_signature']
            individual_photo = request.FILES['individual_photo']

            kin_name = request.POST['kin_name']
            kin_relationship = request.POST['kin_relationship']
            kin_phone = request.POST['kin_phone']
            kin_house_number = request.POST['kin_house_number']
            kin_street_name = request.POST['kin_street_name']
            kin_city = request.POST['kin_city']
            kin_state = request.POST['kin_state']
            kin_country = request.POST['kin_country']
            

            useri = User.objects.create_user(username, individual_email, password)
            useri.is_active=True

            useri.save()

            if joint_account == "Yes":
                joint_account = True
            else:
                joint_account = False


            Send_Email = "trustauthurgroup@gmail.com"
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(Send_Email, 'nxbukvaocrzzetnu')
            mail=server.sendmail


            if individual_email:
                
                a="""Your Email registered successfully"""
                
                msg_chapass = "\r\n".join([
                            
                            "Signup",
                            "",
                            a
                            ]) 

                
                mail(Send_Email,individual_email,msg_chapass)
                messages.success(request,'Email sent')
                print(mail)
                print('yes')



            indiregi = IndividualRegister(user = useri,typeofuser=typeofuser,f_name=f_name,l_name=f_name,phone=phone,house_number=house_number,
            street_name=street_name,city=city, state=state,country=country, birthdate=birthdate,
            gender=gender,occupation=occupation,NIN=NIN,BVN=BVN,
            joint_account=joint_account,individual_signature=individual_signature,individual_photo=individual_photo,
            kin_name=kin_name,kin_relationship=kin_relationship,kin_phone=kin_phone, kin_house_number=kin_house_number, 
            kin_street_name=kin_street_name,kin_city=kin_city,kin_state=kin_state,kin_country=kin_country)

            indiregi.save()

            if joint_account == True:
                another_email = request.POST['another_email']
                another_username = another_email[:another_email.index('@')]
                another_password = request.POST['another_pass']
                another_name = request.POST['another_name']
                another_phone = request.POST['another_phone']
                another_house_number = request.POST['another_house_number']
                another_street_name = request.POST['another_street_name']
                another_city = request.POST['another_city']
                another_state = request.POST['another_state']
                another_country = request.POST['another_country']
                another_birthdate = request.POST['another_birthdate']
                another_gender = request.POST['another_gender']
                another_occupation = request.POST['another_occupation']
                another_signature = request.FILES['another_signature']
                another_photo =   request.FILES['another_photo']


                usera = User.objects.create_user(another_username, another_email, another_password)
                usera.is_active=True

                usera.save()

                another = AnotherJoinAccountRegister(user = usera,individual_user=indiregi,another_name=another_name,
                another_phone=another_phone,another_house_number=another_house_number,
                another_street_name=another_street_name,another_city=another_city, another_state=another_state,
                another_country=another_country, another_birthdate=another_birthdate,another_gender=another_gender,
                another_occupation=another_occupation,another_signature=another_signature,another_photo=another_photo)

                another.save()
        
    return render(request, 'accounts/signup.html')
#    except:
#     return render(request,'accounts/index.html')

def signin(request):
   
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():

            global username
            username = User.objects.get(email=email).username

             
                        
            user = authenticate(username=username, password=password)
            

            if user is not None:
                login(request, user)
                request.session['vendor_email'] = email
                messages.success(request,'You are now logged In Successfully.')
                

                Send_Email = "trustauthurgroup@gmail.com"

                try:
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(Send_Email, 'nxbukvaocrzzetnu')
                    mail=server.sendmail


                    msg_Lin = "\r\n".join([
                        
                    "Subject:Login",
                    "",
                    "You are now logged In Successfully."
                    ])

                    
                    
                    mail(Send_Email,email,msg_Lin)
                    print('yes')
                    return redirect('home')
                except Exception as e :
                    print(e)
                    return redirect('home')       
            else:
                msg = 'Password incorrect'
                return render(request, 'accounts/signin.html',{'msg':msg})
        else:
                msg = 'User does not exist.'
                return render(request, 'accounts/signin.html',{'msg':msg})

    return render(request, 'accounts/signin.html')

def change_password(request,id):
   
  users=User.objects.get(id=id)    
  if request.method =="POST":
     if request.method == "POST":
      
      password=request.POST['password']
      users.set_password(password)
      users.save()
      messages.success(request,'password change Successfully.')
      
      return redirect('signin')
     else:
       
        return render(request,'accounts/Forgotpassword.html')
      
  return render(request,'accounts/Forgotpassword.html')
    
#<----------------------------------------------------->
def change_p(request):
   try:
    if request.method =="POST":
     email = request.POST.get('email')
     Email=User.objects.filter(email=email).exists()
     ide = User.objects.get(email=email).id
     ide=str(ide)
     

     Send_Email = "trustauthurgroup@gmail.com"

     try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(Send_Email, 'nxbukvaocrzzetnu')
        mail=server.sendmail


        if Email:
            ide = User.objects.get(email=email).id
            ide=str(ide)
            a="""Trouble signing in?
            Resetting your password is easy.
            Just press the button below and follow the instructions. Well have you up and running in no time.
            "https://sea-lion-app-wqh6w.ondigitalocean.app/Forgotpassword/"""+ide+"""
            If you did not make this request then please ignore this email."""
            
            msg_chapass = "\r\n".join([
                        
                        "Subject:Change Password",
                        "",
                        """Trouble signing in?
            Resetting your password is easy.
            Just press the button below and follow the instructions. Well have you up and running in no time.
            "https://sea-lion-app-wqh6w.ondigitalocean.app/Forgotpassword/"""+ide+"""
            If you did not make this request then please ignore this email."""
                        
                        ]) 

            
            mail(Send_Email,email,msg_chapass)
            messages.success(request,'Email sent')
            print(mail)
            print('yes')
            return redirect('signin')
     except:
           print('Noo!')
           return redirect('signin')
     else:
        msg = 'Account with that email was not found.'
        return render(request, 'accounts/changepass.html',{'msg':msg})          
   except:
        
        msg = 'Account with that email was not found.'
        
        return render(request, 'accounts/changepass.html',{'msg':msg})          
    
   return render(request,'accounts/changepass.html')

#<------------------------------------------------------>

def Adminchange_p(request,id):
  users=User.objects.get(id=id)
      
  if request.method =="POST":
    if request.method == "POST":
      password=request.POST['passw']
      print(password)
      users.set_password(password)
      users.save()
      messages.success(request,'password change Successfully.')
      return redirect('dev')
   
  else:
       
             
   return render(request,'devadmin/chageFpassword.html')

#<------------------------------------------------------>

def changepassword(request,id): 
  try: 
    user = User.objects.get(id=id)
    cuser = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2= request.POST.get('password2')
        if password1 == password2:
            if user == cuser:
                user.set_password(password1)
                user.save() 
                logout(request)
                messages.success(request, 'Password Changed Successfully.')
                return redirect('sigin')
            else:
                user.set_password(password1)
                user.save() 
                logout(request)
                messages.success(request, 'Password Changed Successfully.')
                return redirect('signin')
        else:
            msg = 'Password are Not Match'
            return render(request,'accounts/changepassword.html',{'msg':msg}) 
 
       
    
    
    return render(request,'accounts/changepassword.html')
  except:
        return redirect('signin')
# <--------------- Notification ---------------->

def Notification(request):
 try:
  if request.method =="POST":
     email = request.POST.get('email')
     Email=User.objects.filter(email=email).exists()
     ide = User.objects.get(email=email).id
     ide=str(ide)
     


     try:
        Send_Email = "trustauthurgroup@gmail.com"
        
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(Send_Email, 'nxbukvaocrzzetnu')
        mail=server.sendmail



        

        
            
        if Email :
            ide = User.objects.get(email=email).id
            ide=str(ide)
            a="""Trouble signing in?
            Resetting your password is easy.
            Just press the button below and follow the instructions. Well have you up and running in no time.
            "https://sea-lion-app-wqh6w.ondigitalocean.app/devadmin/chageFpassword/"""+ide+"""
            If you did not make this request then please ignore this email."""
            
            msg_chapass = "\r\n".join([
                        
                        "Subject:Change Password",
                        "",
                        a
                        ]) 
            
            
            
            mail(Send_Email,email,msg_chapass)
            
            print('yes i am good')
            return redirect('dev')
     except :
        
        print("noooo")
        return redirect('dev')
         
     else:
        msg = 'Email Not Exists!!'
        return render(request, 'devadmin/forgotpassword.html',{'msg':msg})          
 except:
        
        msg = 'Email Not Exists!!!'
        return render(request, 'devadmin/forgotpassword.html',{'msg':msg}) 

 return render(request,'devadmin/forgotpassword.html')
def signout(request):
   try:
    logout(request)
    messages.success(request,'You are logged out Successfully.')
    
    
    
    return redirect('signin')
   except:
    return render(request,'accounts/index.html')
def product(request):
   try:
    product = Product.objects.all()
    if request.user.is_authenticated:  
        if IndividualRegister.objects.filter(user=request.user).exists():
            cuser = IndividualRegister.objects.get(user=request.user)
            product = Product.objects.filter(typeofuser=cuser.typeofuser)
        elif BusinessRegister.objects.filter(user=request.user).exists():
            cuser = BusinessRegister.objects.get(user=request.user)
            product = Product.objects.filter(typeofuser=cuser.typeofuser)
        else:
            product = Product.objects.all()
        return render(request, 'accounts/product.html',{'product':product})

    return render(request, 'accounts/product.html',{'product':product})
   except:
    return render(request,'accounts/index.html')
def subproduct(request,id):
   
   
    logged_id = False
    query = ''
    product = Product.objects.get(id=id)
    
    if request.user.is_authenticated:
        logged_id = True
    
    print(logged_id)
    if logged_id == False:
        query = "select * from accounts_subproduct where Scope = 'Public' and product_id =  "+ str(id)
    else :
        # cuser =User.objects.get(id=request.user)
        print(request.user.id)
        query = """select * from accounts_subproduct where Scope = 'Public' and product_id =  """+ str(id) + """
union
select accounts_subproduct.* from accounts_assign_products join accounts_subproduct on accounts_assign_products.product_id =  accounts_subproduct.id where accounts_assign_products.user_id = """+ str(request.user.id) +""" and accounts_subproduct.product_id = """ + str(id)
    



    subproduct = SubProduct.objects.raw(query)


    # if SubProduct.objects.get(Scope = 'private'):
    #  subproduct = SubProduct.objects.filter(product=product)   
    #  print ('farahn')
    # else:SubProduct.objects.filter(product=product) and
   


    # if request.user.is_authenticated:
      
    #    cuser =User.objects.get(username=request.user)
    #    subproduct =   SubProduct.objects.filter(Scope = 'Public' , product=product ).union(SubProduct.objects.filter(Assign=cuser , product=product))

    # else:
    #     subproduct =   SubProduct.objects.filter(Scope = 'Public' )


      
    # print (subproduct )
    return render(request, 'accounts/subproduct.html',{'product':product,'subproduct':subproduct})
 
def productdetail(request,id):
   try:
    #product = SubProduct.objects.get(id=id)
    product = SubProduct.objects.raw("SELECT  accounts_product.title category_title,  * FROM accounts_subproduct JOIN accounts_product on accounts_product.id = accounts_subproduct.product_id where accounts_subproduct.id = "+ str(id))

    global uui
    uui = str(uuid.uuid1())
    uui = uui[:6]
    print(uui)
    print(product[0])
 
  

    subproductall = SubProduct.objects.filter(product=product[0].product)
    s = {}
    s1 = "abc:wertasdfgfdsvb sdf asdfg#def:asdf qwert asdfg asdf"
    for i in s1.split('#'):
        s.update({i.split(":")[0]:i.split(":")[1]})
    return render(request, 'accounts/productDetail.html',{'dic':s,'product':product [0],'subproductall':subproductall,'uui':uui})

   except Exception as e:
    print(e)
    return render(request,'accounts/index.html')

def contact(request):
   try:
    home = HomeInfoSection.objects.all().last()
    if request.method =="POST":
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        contact= request.POST.get('phone','')
        message= request.POST.get('message','')
        Contact(name=name, email=email, contact=contact, message=message).save()
        messages.success(request,'Your feedback has been submitted successfully')
        return redirect("home")

    return render(request, 'accounts/contact.html',{'home':home})
   except:
    return render(request,'accounts/index.html')

def subscriber(request):
   try:
    subscribeusers = Subscriber.objects.all()
    subemail = []

    for i in subscribeusers:
        subemail.append(i.email)

    if request.method =="POST":
        email= request.POST.get('email','')
        if email not in subemail:
            Subscriber(email=email).save()
            messages.success(request,'You have successfully subscribed to our newsletter')
            return redirect("home")
        else:
            messages.error(request,"You're already Subscribed.")
            return redirect("home")
   except:
    return render(request,'accounts/index.html')

def dev(request):
 try:  
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            return render(request, 'devadmin/index.html')
        else:
            logout(request)
            return redirect('dev')
        
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        if User.objects.filter(email=email).exists():
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_superuser == True or user.is_staff == True:
                    login(request, user)
                    messages.success(request,'You are now logged In.')

                    Send_Email = "trustauthurgroup@gmail.com"

                    try:
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login(Send_Email, 'nxbukvaocrzzetnu')
                        mail=server.sendmail


                        msg_Lin = "\r\n".join([
                            
                        "Subject:Login",
                        "",
                        "You are now logged In Successfully."
                        ])
 
                        mail(Send_Email,email,msg_Lin)
                        
                        return redirect('dashboard')
                    except:
                     
                     return redirect('dashboard')
                else:
                    messages.error(request,'User Not Exists!!!')
                    msg = 'User Not Exists!!!'
                    return render(request, 'devadmin/login.html',{'msg':msg})    
                
            else:
                msg = 'User Not Exists!!!'
                messages.error(request,'User Not Exists!!!')
                return render(request, 'devadmin/login.html',{'msg':msg})
        
        else:
            msg = 'User does not exist'
            return render(request, 'devadmin/login.html',{'msg':msg})

    return render(request, 'devadmin/login.html')
 except:
    return render(request, 'devadmin/login.html')
def addadmin(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2= request.POST.get('password2')

        if request.POST.get('superadmin',''):
            superadmin = True
        else:
            superadmin = False

        if request.POST.get('admin',''):
            admin = True
        else:
            admin = False


        if password1 == password2:

            users = User.objects.all()
            user = []

            for i in users:
                user.append(i.email)

            if email not in user:
                username = email[:email.index('@')]
                user = User.objects.create_user(username, email, password1)

                user.is_active=True

                if superadmin == True:
                    user.is_superuser = True
                   
                else:
                    user.is_superuser = False 

                if admin == True:
                    user.is_staff = True
                else:
                    user.is_staff = False

                user.save()
                messages.success(request, 'Added Successfully.')

                return redirect('adminlist')
            else:
                msg = 'Email Already Exists23!!!'
                return render(request, 'devadmin/addadmin.html',{'msg':msg})
        else:
            msg = 'Password are Not Match'
            return render(request, 'devadmin/addadmin.html',{'msg':msg})

    return render(request, 'devadmin/addadmin.html')

def adminlist(request):

    admin = User.objects.filter(Q(is_superuser = True)| Q(is_staff = True))
    return render(request, 'devadmin/adminlist.html',{'admin':admin})

def admindelete(request,id):

    user = User.objects.get(pk=id)
    user.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('adminlist')


def adminchangepass(request,id):
   
    user = User.objects.get(id=id)
    cuser = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2= request.POST.get('password2')
        if password1 == password2:
            if user == cuser:
                user.set_password(password1)
                user.save() 
                logout(request)
                messages.success(request, 'Password Changed Successfully.')
                return redirect('dev')
            else:
                user.set_password(password1)
                user.save() 
                messages.success(request, 'Password Changed Successfully.')
                return redirect('adminlist')
        else:
            msg = 'Password are Not Match'
            return render(request, 'devadmin/adminchangepass.html',{'msg':msg})

    return render(request, 'devadmin/adminchangepass.html')


def adminedit(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':

        users = User.objects.all()
        userlist = []

        for i in users:
            userlist.append(i.email)

        email = request.POST.get('email')
        if email not in users:

            user.email = email
            user.username = email[:email.index('@')]

            if request.POST.get('superadmin',''):
                superadmin = True
            else:
                superadmin = False

            if request.POST.get('admin',''):
                admin = True
            else:
                admin = False

            if superadmin == True:
                user.is_superuser = True
            else:
                user.is_superuser = False

            if admin == True:
                user.is_staff = True
            else:
                user.is_staff = False

            user.save()
            messages.success(request, 'Updated Successfully.')
            E_Message="Updated Successfully."

            Send_Email = "trustauthurgroup@gmail.com"


            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(Send_Email, 'nxbukvaocrzzetnu')

            mail=server.sendmail


            mail(Send_Email,email,E_Message)
            return redirect('adminlist')
        else:
            msg = 'Email Already Exists11!!!'
            return render(request, 'devadmin/adminedit.html',{'msg':msg})

    return render(request, 'devadmin/adminedit.html',{'user':user})


def adminlogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully.')
    return redirect('dev')


def dashboard(request):
   
    product = SubProduct.objects.all()
    corporatecount = BusinessRegister.objects.all().count()
    individualcount = IndividualRegister.objects.all().count()

    orders = OrderPlaced.objects.filter(payment_status='paid')

    print(orders)
    

    camount = 0
    iamount = 0
    # for i in orders:
    #     if i.product.product.typeofuser == 'corporate':
    #         camount = camount + i.price
    #     elif i.product.product.typeofuser == 'individual':
    #         iamount = iamount + i.price

    if request.method == "POST":
        titleofproduct = request.POST['typeofproduct']
        product = SubProduct.objects.get(sub_title=titleofproduct)
        mindate = request.POST['mindate']
        maxdate = request.POST['maxdate']
        orders = OrderPlaced.objects.filter(product=product)
        print(product)
        return render(request, 'devadmin/monthlyfilter.html',{'orders':orders,'mindate':mindate,'maxdate':maxdate})
   
    return render(request, 'devadmin/index.html',{'product':product,'corporatecount':corporatecount,'camount':camount,'individualcount':individualcount,'iamount':iamount})
   
def monthlyfilter(request):
    order = OrderPlaced.objects.all()
    return render(request, 'devadmin/monthlyfilter.html',{'orders':order})

def admincontactlist(request):
    contact = Contact.objects.all()
    return render(request, 'devadmin/admincontactlist.html',{'contact':contact})

def admincontact(request,id):
    curcontact = Contact.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get('fluency',''):
            checked = True
        else:
            checked = False

        curcontact.checked = checked
        curcontact.save()
        return redirect('admincontactlist')

def adminsubscriberlist(request):
    subscriber = Subscriber.objects.all()
    return render(request, 'devadmin/adminsubscriberlist.html',{'subscriber':subscriber})

def adminaddproduct(request):

    typeofuser_selection = ['corporate','individual']
    if request.method == "POST":
        typeofuser = request.POST.get('typeofuser','')
        title = request.POST.get('title','')
        title2 = request.POST.get('title2','')
        product_image = request.FILES['productpic']
        Product(typeofuser=typeofuser, title=title, title2=title2, product_image=product_image).save()
        messages.success(request, 'Product Added Successfully.')
        return redirect('adminproductlist')

    return render(request, 'devadmin/addproduct.html',{'typeofuser':typeofuser_selection})


def admineditproduct(request,id):
    typeofuser_selection = ['corporate','individual']
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.typeofuser= request.POST.get('typeofuser','')
        product.title= request.POST.get('title','')
        product.title2= request.POST.get('title2','')
        productpic = request.FILES.get('productpic')
        if productpic is not None:
            product.product_image = productpic

        product.save()
        messages.success(request, 'Product Updated Successfully.')
        return redirect('adminproductlist')

    return render(request, 'devadmin/admineditproduct.html',{'product':product,'typeofuser':typeofuser_selection})

def admindeleteproduct(request,id):

    pi = Product.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Product Deleted Succesfully.')
    return redirect('adminproductlist')


def adminaddsubproduct(request):
  try:
    product = Product.objects.all()
    dat=datetime.date.today()
    print(dat)
    if request.method == "POST":
        titleofproduct = request.POST['typeofproduct']
        
        product = Product.objects.get(title=titleofproduct)
        sub_title = request.POST['subtitle']
        sub_title2 = request.POST['subtitle2']
        
        selling_price = request.POST['selling_price']
        Total_stock =   request.POST['Total']
      
        Rate = request.POST['Rate'] 
        Principle = request.POST['Principle'] 
        # Date = request.POST['Date']
        Date = dat
               
        Minemun_Order = request.POST['Minemum']
        duration_month = request.POST['duration_month']
        duration_year = request.POST['duration_year']
        benifits = request.POST['benifits']
        plan_feature = request.POST['planfeatures']
        sub_product_image = request.FILES['productpic'] 
        Scope = request.POST['scopeofproduct']
        SubProduct(product=product, sub_title=sub_title, sub_title2=sub_title2, selling_price=selling_price, Total_S=Total_stock, Minemun_O=Minemun_Order,Rate=Rate,
        benifits=benifits,plan_feature=plan_feature,sub_product_image=sub_product_image,duration_month=duration_month, Scope=Scope,Principle=Principle,Date=Date,
        duration_year=duration_year).save()
        messages.success(request, 'SubProduct Added Successfully.')
        return redirect('adminsubproductlist')

    return render(request, 'devadmin/addsubproduct.html',{'product':product,'dat':dat})
  except Exception as e:
    print(e)
def admineditsubproduct(request,id):
    product = Product.objects.all()
    subproduct = SubProduct.objects.get(id=id)
    if request.method == 'POST':
        titleofproduct= request.POST.get('typeofproduct','')
        subproduct.product = Product.objects.get(title=titleofproduct)
        subproduct.title= request.POST.get('sub_title','')
        subproduct.title2= request.POST.get('sub_title2','')
        subproduct.selling_price= request.POST.get('selling_price','')
        subproduct.Total_S =   request.POST['Total']
        subproduct.Minemun_O = request.POST['Minemum']
        subproduct.duration_month= request.POST.get('duration_month','')
        subproduct.duration_year= request.POST.get('duration_year','')
        subproduct.benifits= request.POST.get('benifits','')
        subproduct.plan_feature= request.POST.get('planfeatures','')
        subproductpic = request.FILES.get('productpic')
        if subproductpic is not None:
            subproduct.sub_product_image = subproductpic

        subproduct.save()
        messages.success(request, 'SubProduct Updated Successfully.')
        return redirect('adminsubproductlist')

    return render(request, 'devadmin/admineditsubproduct.html',{'subproduct':subproduct,'product':product})

def admindeletesubproduct(request,id):

    pi = SubProduct.objects.get(pk=id)
    pi.delete()
    messages.success(request,'SubProduct Deleted Succesfully.')
    return redirect('adminsubproductlist')

def adminproductlist(request):

    product = Product.objects.all()
    
    
    return render(request, 'devadmin/adminproductlist.html',{'product':product})


def adminsubproductlist(request):
    subproduct = SubProduct.objects.all()

  
    return render(request, 'devadmin/adminsubproductlist.html',{'subproduct':subproduct})

def adminabusinessusers(request):
    busers = BusinessRegister.objects.all()
    return render(request, 'devadmin/adminabusinessusers.html',{'busers':busers})

def buserextradetails(request,id):
    busers = BusinessRegister.objects.get(id=id)
    return render(request, 'devadmin/buserextradetails.html',{'busers':busers})

def adminaindividualusers(request):
    iusers = IndividualRegister.objects.raw('SELECT  auth_user.email u_email,  * FROM accounts_individualregister JOIN auth_user on auth_user.id = accounts_individualregister.user_id where accounts_individualregister.joint_account = false')
    return render(request, 'devadmin/adminaindividualusers.html',{'iusers':iusers})

def iuserextradetails(request,id):
    iusers = IndividualRegister.objects.get(id=id)
    return render(request, 'devadmin/iuserextradetails.html',{'iuser':iusers})

def adminaindividualjointusers(request):
    ijusers = AnotherJoinAccountRegister.objects.all()
    return render(request, 'devadmin/adminaindividualjointusers.html',{'ijusers':ijusers})

def ijuserextradetails(request,id):
    ijusers = AnotherJoinAccountRegister.objects.get(id=id)
    return render(request, 'devadmin/ijuserextradetails.html',{'ijusers':ijusers})

def admincustomers(request):
    order = OrderPlaced.objects.all()
    return render(request, 'devadmin/admincustomer.html',{'order':order})

def transaction(request):
    status = ['paid','pending','fail']
    order = OrderPlaced.objects.all()
    return render(request, 'devadmin/admintransaction.html',{'orders':order,'status':status})

def transactionupdate(request,id):
    status = ['paid','pending','fail']
    order = OrderPlaced.objects.get(id=id)
    
    if request.method == "POST":
        payment_status = request.POST.get('payment_status','')
        payment_id = request.POST.get('payment_id','')
        order.payment_status = payment_status
        order.payment_id = payment_id
        order.save()
        if order.payment_status == 'paid':
            print('aliiiiiii')
            SubProduct.objects.filter(id = productid).update(Total_S = total_quan)
        
        return redirect('transaction')
    return render(request, 'devadmin/updatetransaction.html',{'orders':order,'status':status})

def adminquote(request):
    quote = Quote.objects.all()
    return render(request, 'devadmin/adminquote.html',{'quote':quote})


def homebanner(request):
   try:
    banner = HomeBanner.objects.all()
    return render(request, 'devadmin/homebanner.html',{'banner':banner})
   except:
    return render(request,'accounts/index.html')
def addhomebanner(request):

   try:
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        banner_image = request.FILES['banner_image']
        HomeBanner(title=title, description=description, banner_image=banner_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('homebanner')

    return render(request, 'devadmin/addhomebanner.html')
   except:
    return render(request,'accounts/index.html')

def edithomebanner(request,id):
   try:
    banner = HomeBanner.objects.get(id=id)
    if request.method == 'POST':
        banner.title= request.POST.get('title','')
        banner.description= request.POST.get('description','')
        banner_image = request.FILES.get('banner_image')
        if banner_image is not None:
            banner.banner_image = banner_image

        banner.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('homebanner')

    return render(request, 'devadmin/edithomebanner.html',{'banner':banner})
   except:
    return render(request,'accounts/index.html')
def deletehomebanner(request,id):
   try:
    pi = HomeBanner.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('homebanner')
   except:
    return render(request,'accounts/index.html')

def homexploreproducts(request):
   try:
    explore = HomeExploreProducts.objects.all()
    return render(request, 'devadmin/homexploreproducts.html',{'explore':explore})
   except:
    return render(request,'accounts/index.html')
def addexploreproduct(request):
   try:
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        exp_image = request.FILES['exp_image']
        HomeExploreProducts(title=title, description=description, exp_image=exp_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('homexploreproducts')

    return render(request, 'devadmin/addexploreproduct.html')
   except:
    return render(request,'accounts/index.html')

def editexploreproduct(request,id):
   try:
    explore = HomeExploreProducts.objects.get(id=id)
    if request.method == 'POST':
        explore.title= request.POST.get('title','')
        explore.description= request.POST.get('description','')
        exp_image = request.FILES.get('exp_image')
        if exp_image is not None:
            explore.exp_image = exp_image

        explore.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('homexploreproducts')

    return render(request, 'devadmin/editexploreproduct.html',{'explore':explore})
   except:
    return render(request,'accounts/index.html')
def deleteexploreproduct(request,id):
   try:
    pi = HomeExploreProducts.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('homexploreproducts')
   except:
    return render(request,'accounts/index.html')

def hometestinomials(request):
   try:
    testi = HomeTestinomials.objects.all()
    return render(request, 'devadmin/hometestinomials.html',{'testi':testi})
   except:
    return render(request,'accounts/index.html')
def addhometestinomials(request):
   try:
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        testi_image = request.FILES['testi_image']
        HomeTestinomials(name=name, description=description, testi_image=testi_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('hometestinomials')

    return render(request, 'devadmin/addhometestinomials.html')
   except:
    return render(request,'accounts/index.html')

def edithometestinomials(request,id):
   try:
    testi = HomeTestinomials.objects.get(id=id)
    if request.method == 'POST':
        testi.name= request.POST.get('name','')
        testi.description= request.POST.get('description','')
        testi_image = request.FILES.get('testi_image')
        if testi_image is not None:
            testi.testi_image = testi_image

        testi.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('hometestinomials')

    return render(request, 'devadmin/edithometestinomials.html',{'testi':testi})
   except:
     return render(request,'accounts/index.html')
def deletehometestinomials(request,id):
   try:
    pi = HomeTestinomials.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('hometestinomials')
   except:
    return render(request,'accounts/index.html')

def homewhatwedo(request):
   try:
    wwd = HomeWhatWeDo.objects.all()
    return render(request, 'devadmin/homewhatwedo.html',{'wwd':wwd})
   except:
    return render(request,'accounts/index.html')
def addhomewhatwedo(request):
   try:
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        icon_image = request.FILES['icon_image']
        icon_image_hover = request.FILES['icon_image_hover']
        HomeWhatWeDo(name=name, description=description, icon_image=icon_image,icon_image_hover=icon_image_hover).save()
        messages.success(request, 'Added Successfully.')
        return redirect('homewhatwedo')

    return render(request, 'devadmin/addhomewhatwedo.html')
   except:
    return render(request,'accounts/index.html')

def edithomewhatwedo(request,id):
   try:
    wwd = HomeWhatWeDo.objects.get(id=id)
    if request.method == 'POST':
        wwd.name= request.POST.get('name','')
        wwd.description= request.POST.get('description','')
        icon_image = request.FILES.get('icon_image')
        icon_image_hover = request.FILES.get('icon_image_hover')
        if icon_image is not None:
            wwd.icon_image = icon_image
        if icon_image_hover is not None:
            wwd.icon_image_hover = icon_image_hover

        wwd.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('homewhatwedo')

    return render(request, 'devadmin/edithomewhatwedo.html',{'wwd':wwd})
   except:
    return render(request,'accounts/index.html')
def deletehomewhatwedo(request,id):
   try:
    pi = HomeWhatWeDo.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('homewhatwedo')
   except:
    return render(request,'accounts/index.html')

def homeinfosection(request):
   try:
    home= HomeInfoSection.objects.all().last()
    if request.method == 'POST':
        home.home_box1_title= request.POST.get('home_box1_title','')
        home.box1_description= request.POST.get('box1_description','')
        home.home_box2_title= request.POST.get('home_box2_title','')
        home.box2_description= request.POST.get('box2_description','')
        home.home_box3_title= request.POST.get('home_box3_title','')
        home.box3_description= request.POST.get('box3_description','')
        # home.about_head= request.POST.get('about_head','')
        # home.about_description= request.POST.get('about_description','')
        # home.about_mission= request.POST.get('about_mission','')
        # home.about_vision= request.POST.get('about_vision','')
        # home.about_commitment= request.POST.get('about_commitment','')
        home.hotline= request.POST.get('hotline','')
        home.email= request.POST.get('email','')
        home.market_update= request.POST.get('market_update','')
        home.news= request.POST.get('news','')
        home.sectornews= request.POST.get('sectornews','')
        home.upcomingevents= request.POST.get('upcomingevents','')
        # about_image = request.FILES.get('about_image')
        contact_image = request.FILES.get('contact_image')

        if contact_image is not None:
            home.contact_image = contact_image
        # if about_image is not None:
        #     home.about_image = about_image

        home.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('homeinfosection')

    return render(request, 'devadmin/homeinfosection.html',{'home':home})
   except:
    return render(request,'accounts/index.html')



def aboutinfosection(request):
   try:
    about = AboutInfoSection.objects.all().last()
    if request.method == 'POST':
        about.about_description= request.POST.get('about_description','')
        about.about_description2= request.POST.get('about_description2','')
        about.about_description3= request.POST.get('about_description3','')
        about_image = request.FILES.get('about_image')
        if about_image is not None:
            about.about_image = about_image

        about.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('aboutinfosection')

    return render(request, 'devadmin/aboutinfosection.html',{'about':about})
   except:
    return render(request,'accounts/index.html')


def abouttestinomials(request):
   try:
    testi = AboutTestinomials.objects.all()
    return render(request, 'devadmin/abouttestinomials.html',{'testi':testi})
   except:
    return render(request,'accounts/index.html')

def addabouttestinomials(request):
   try:
    if request.method == "POST":
        name = request.POST['name']
        profession = request.POST['profession']
        description = request.POST['description']
        testi_image = request.FILES['testi_image']
        AboutTestinomials(name=name, description=description,profession=profession ,testi_image=testi_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('abouttestinomials')

    return render(request, 'devadmin/addabouttestinomials.html')
   except:
    return render(request,'accounts/index.html')


def editabouttestinomials(request,id):
   try:
    testi = AboutTestinomials.objects.get(id=id)
    if request.method == 'POST':
        testi.name= request.POST.get('name','')
        testi.profession= request.POST.get('profession','')
        testi.description= request.POST.get('description','')
        testi_image = request.FILES.get('testi_image')
        if testi_image is not None:
            testi.testi_image = testi_image

        testi.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('abouttestinomials')

    return render(request, 'devadmin/editabouttestinomials.html',{'testi':testi})
   except:
    return render(request,'accounts/index.html')

def deleteabouttestinomials(request,id):
   try:
    pi = AboutTestinomials.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('abouttestinomials')
   except:
    return render(request,'accounts/index.html')


def aboutcompanycore(request):
   try:
    ccv = AboutCompanyCore.objects.all()
    return render(request, 'devadmin/aboutcompanycore.html',{'ccv':ccv})
   except:
    return render(request,'accounts/index.html')

def addaboutcompanycore(request):
   try:
    if request.method == "POST":
        description = request.POST['description']
        core_image = request.FILES['core_image']
        AboutCompanyCore(description=description, core_image=core_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('aboutcompanycore')

    return render(request, 'devadmin/addaboutcompanycore.html')
   except:
    return render(request,'accounts/index.html')


def editaboutcompanycore(request,id):
   try:
    ccv = AboutCompanyCore.objects.get(id=id)
    if request.method == 'POST':
        ccv.description= request.POST.get('description','')
        core_image = request.FILES.get('core_image')
        if core_image is not None:
            ccv.core_image = core_image

        ccv.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('aboutcompanycore')

    return render(request, 'devadmin/editaboutcompanycore.html',{'ccv':ccv})
   except:
    return render(request,'accounts/index.html')

def deleteaboutcompanycore(request,id):
   try:
    pi = AboutCompanyCore.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('aboutcompanycore')
   except:
    return render(request,'accounts/index.html')

def aboutteammember(request):
   try:
    member = AboutTeamMembers.objects.all()
    return render(request, 'devadmin/aboutteammember.html',{'member':member})
   except:
    return render(request,'devadmin/aboutteammember.html')

def aboutboardmembers(request):
    print("aboutboardmembers")
    b_member = AboutBoardMembers.objects.all()
    print(b_member)
    return render(request, 'devadmin/aboutboardmember.html',{'b_member':b_member})

def addaboutteammember(request):
   try:
    if request.method == "POST":
        name = request.POST['name']
        profession = request.POST['profession']
        description = request.POST['description']
        member_image = request.FILES['member_image']
        AboutTeamMembers(name=name,profession=profession ,description=description,member_image=member_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('aboutteammember')

    return render(request, 'devadmin/addaboutteammember.html')
   except:
    return render(request,'devadmin/addaboutteammember.html')

def addaboutboardmember(request):

    if request.method == "POST":
        name = request.POST['name']
        profession = request.POST['profession']
        description = request.POST['description']
        member_image = request.FILES['member_image']
        AboutBoardMembers(name=name,profession=profession ,description=description,member_image=member_image).save()
        messages.success(request, 'Added Successfully.')
        return redirect('aboutboardmembers')    

    return render(request, 'devadmin/addaboutboardmember.html')

def editaboutteammember(request,id):
   try:
    member = AboutTeamMembers.objects.get(id=id)
    if request.method == 'POST':
        member.name= request.POST.get('name','')
        member.profession= request.POST.get('profession','')
        member.description= request.POST.get('description','')
        member_image = request.FILES.get('member_image')
        if member_image is not None:
            member.member_image = member_image

        member.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('aboutboardmember')

    return render(request, 'devadmin/editaboutteammember.html',{'member':member})
   except Exception as e:
    print (e)
    return render(request,'devadmin/editaboutteammember.html')


def editaboutboardmember(request,id):
   try:
    b_member = AboutBoardMembers.objects.get(id=id)
    print('farhan')
    if request.method == 'POST':
        b_member.name= request.POST.get('name','')
        b_member.profession= request.POST.get('profession','')
        b_member.description= request.POST.get('description','')
        member_image = request.FILES.get('member_image')
        if member_image is not None:
            b_member.member_image = member_image

        b_member.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('aboutboardmembers')

    return render(request, 'devadmin/addaboutboardmember.html',{'member':b_member})
   except Exception as e:
    
    print(e)




def deleteaboutteammember(request,id):
   
    pi = AboutTeamMembers.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('aboutteammember')
   
def deleteaboutboardmember(request,id):
   
    pi = AboutBoardMembers.objects.get(pk=id)
    print(pi)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('aboutboardmembers')
   


def quote(request):
#       
    if request.method == "POST":
        user = request.user
        productid = request.POST['product-id']
   
        quan = request.POST['u_quan']
    
        
        Total_p = request.POST['total_p']
        try:
         quote_date = request.POST['starting_date_q']
         frequency = request.POST['frequency_q'] 
         print(quote_date)
        except:
         quote_date = date.today()
         frequency = "null"
        print(frequency) 
       

        product_check = SubProduct.objects.get(id=productid)
        if(product_check):
            if(Quote.objects.filter(user=user,product_id = productid, total_p = Total_p )):
                messages.info(request, 'Its Already Quoted.')
            else:
               if quan != 0 and frequency == "null":
                   Quote.objects.create(user=user,product_id = productid,quote_quantity = quan,quote_date=date.today() ,total_p = Total_p )
                   messages.success(request, 'Quoted Successfully.')
            #    elif request.POST['frequency_q'] == 'null': 
            #     Quote.objects.create(user=user,product_id = productid,quote_quantity = quan, total_p = Total_p )
            #     messages.success(request, 'Quoted Successfully.')
               else:
                Quote.objects.create(user=user,product_id = productid,frequency=frequency,quote_date=quote_date, total_p = Total_p )
                messages.success(request, 'Quoted Successfully.')
        else:
            messages.error("No Such Product")

    return redirect('customerquote')
#    except Exception as e:

#     print(e)

    return render(request,'accounts/index.html')


def adminnewslist(request):
   try:
    news = News.objects.all()
    return render(request, 'devadmin/adminnewslist.html',{'news':news})
   except:
    return render(request,'accounts/index.html')

def adminaddnews(request):
   try:
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        doc = request.POST['doc']
        newspic = request.FILES['newspic']
        News(title=title,description=description ,newspic=newspic,doc=doc).save()
        messages.success(request, 'Added Successfully.')
        return redirect('adminnewslist')

    return render(request, 'devadmin/adminaddnews.html')
   except:
    return render(request,'devadmin')


def admineditnews(request,id):
   try:
    news = News.objects.get(id=id)
    if request.method == 'POST':
        news.title= request.POST.get('title','')
        news.description= request.POST.get('description','')
        news.doc= request.POST.get('doc','')
        newspic = request.FILES.get('newspic')
        if newspic is not None:
            news.newspic = newspic

        news.save()
        messages.success(request, 'Updated Successfully.')
        return redirect('adminnewslist')

    return render(request, 'devadmin/admineditnews.html',{'news':news})
   except:
    return render(request,'accounts/index.html')

def admindeletenews(request,id):
   try:
    pi = News.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Deleted Succesfully.')
    return redirect('adminnewslist')
   except:
    return render(request,'accounts/index.html')



# import stripe
# from django.http import HttpResponse
# # This is your test secret API key.
# stripe.api_key = 'sk_test_51LI4MfSA0EQlpaFH4u9eKOMnsKxhRqasqmfhJf4WHkYQ3brrtuPAjsou1ivccakPwuHvBjG95DZOhytEAoR9xGbK00W4JKRWyY'

from dateutil.relativedelta import relativedelta
def offlinepayment(request):
  

    if request.method == "POST":
        global productid
        productid = request.POST['product-id']
        product = SubProduct.objects.get(id=productid)
        global qua
        qua = request.POST['U_product']
        global total_price 
        total_price = request.POST['total_price']
      
        global total_quan
        try:
         
         total_quan = request.POST['product_quantity']
   
        except:
         
         total_quan = product.Total_S - int(total_price)
        
        global frequenc
        Frequency=request.POST['frequency_OF']
        
        if Frequency in ["Monthly","Quarterly","Annually"]:
          frequenc = request.POST['frequency_OF'] 
          
          frequency = frequenc
        else:
          frequenc = request.POST['frequency_OF']
          frequenc = 'null'
          frequency = frequenc

        product = SubProduct.objects.get(id=productid)
        if Quote.objects.filter(user=request.user,product_id = productid).exists():
            quote = Quote.objects.get(user=request.user,product_id = productid)
            quote.delete()
        product_title = product.sub_title
        price = product.selling_price
        now = date.today()
        
        

        try:

            duedate = now + relativedelta(months = int(product.duration_month))
            duedate = duedate + relativedelta(years = int(product.duration_year))
      
        except:
         
            now = date.today()
            if frequency == 'Quarterly':
        
            #  frequency = "3"
               duedate = now + relativedelta(months=+3)
            elif frequency == 'Monthly':
                # frequency = "1"                
                duedate = now + relativedelta(months=+1)
            elif frequency == 'Annually':
                
                # frequency = "12"                
                duedate = now + relativedelta(months=+1)
               
            else:
                 duedate = now + relativedelta(months = int(product.duration_month))
                 duedate = duedate + relativedelta(years = int(product.duration_year))

        order = OrderPlaced.objects.create(user=request.user, product=product,product_title=product_title,price=total_price,frequency=frequenc,
                                            payment_id = uui,quantity=qua,modeofpayment='offline',payment_status='pending',
                                            due_date=duedate)
        order.save()
        #SubProduct.objects.filter(id = productid).update(Total_S=Totsl_S-U_Product)
        messages.success(request,'Your Request is Submitted. Trustbanc Contact you as soon as.')
        return redirect('orders')
#   except Exception as e:
#     print(e)
#     return redirect('orders')

import requests
import json
from django.http import HttpResponseRedirect
def checkout(request):
   
    host = request.get_host()
    
    if request.method == "POST":
        
        global productid
        productid = request.POST['product-id']
        global R_Product
        R_Product = request.POST['avail_pro']
        global U_Product
        U_Product = request.POST['U_product']
        
        print(U_Product)
       
        global frequenc
        try:
         
         frequenc = request.POST['frequency_O'] 
         
         frequency = frequenc
        except:
         frequency = "null"
         

        product = SubProduct.objects.get(id=productid)
        if Quote.objects.filter(user=request.user,product_id = productid).exists():
            quote = Quote.objects.get(user=request.user,product_id = productid)
            quote.delete()
        product_title = product.sub_title
        if product.selling_price != 0 :
          price = product.selling_price
        else:
          price = product.Rate  
        
        
        now = datetime.date.today()
      
        try:

            duedate = now + relativedelta(months = int(product.duration_month))
            duedate = duedate + relativedelta(years = int(product.duration_year))
           
        except:
             now = date.today()
             if frequency == 'Quarterly':
              frequency = "3"
              duedate = now + relativedelta(months=+3)
             elif frequency == 'Monthly':
                
                frequency = "1"                

                duedate = now + relativedelta(months=+1)
                

             elif  frequency  == 'Annually':
                 frequency =  "12" 
                 duedate = now + relativedelta(months=+12)
      
            
        # OrderPlaced.objects.filter(productid=productid).update(quantity=U_Product)

        # checkout_session = stripe.checkout.Session.create(
        #     line_items=[
        #         {
        #             # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
        #             'price_data':{
        #                 'currency':'INR',
        #                 'unit_amount':int(product.selling_price) * 100,
        #                 'product_data':{
        #                     'name':order.id,
        #                 },
        #             },
        #             'quantity': 1,
        #         },
        #     ],
        #     mode='payment',
        #     success_url = "http://{}{}".format(host,reverse('paymentsuccess')),
        #     cancel_url = "http://{}{}".format(host,reverse('paymentcancel')),
        # )

        # return redirect(checkout_session.url, code=303)
   
      
        def init_payment(request):

            url = 'https://api.paystack.co/transaction/initialize'
            headers = {
                'Authorization': 'Bearer '+settings.PAYSTACK_SECRET_KEY,
                'Content-Type' : 'application/json',
                'Accept': 'application/json',
                }
            try:  
             if U_Product == 0 : 
              pro = (int(U_Product))
             else:
              pro =(int(frequency))
            except:
                pro = (int(U_Product))
            datum = {
                "email": request.user.email,
                "amount": int(price*pro) * 100
                }

            
           
            x = requests.post(url, data=json.dumps(datum), headers=headers)
          
            if x.status_code != 200:
                return str(x.status_code)

            results = x.json()

            return results
       

        initialized = init_payment(request)
            
        order = OrderPlaced.objects.create(user=request.user, product=product,product_title=product_title,price=price,frequency=frequenc,
                                            modeofpayment='online',due_date=duedate,payment_status='pending',payment_id=initialized['data']['reference'])
        order.save()
        amount = price/100
        link = initialized['data']['authorization_url']
        return HttpResponseRedirect(link)
        #return redirect(orders)


def call_back_url(request):
    

    reference = request.GET.get('reference')

	# We need to fetch the reference from PAYMENT
    check_pay = OrderPlaced.objects.filter(payment_id=reference).exists()
    
    if check_pay == False:
		# This means payment was not made error should be thrown here...
        print("Error")
    else:
        payment = OrderPlaced.objects.get(payment_id=reference)
        
        def verify_payment(request):
            print("hello")
            url = 'https://api.paystack.co/transaction/verify/'+reference
            
            headers = {
				'Authorization': 'Bearer '+settings.PAYSTACK_SECRET_KEY,
				'Content-Type' : 'application/json',
				'Accept': 'application/json',
				}
            datum = {
				"reference": payment.payment_id
				}
            x = requests.get(url, data=json.dumps(datum), headers=headers)
            
            if x.status_code != 200:
                return str(x.status_code)

            results = x.json()
            return results

    initialized = verify_payment(request)
    if initialized['data']['status'] == 'success':
       OrderPlaced.objects.filter(payment_id=initialized['data']['reference']).update(payment_status='paid')
       OrderPlaced.objects.filter(payment_id=initialized['data']['reference']).update(quantity=U_Product)
       if OrderPlaced.objects.filter(payment_status='paid'):
         try:
          SubProduct.objects.filter(id=productid).update(Total_S=R_Product)
         except:
          print(productid)
          
        
       

       return redirect('orders')
    
    return render(request, 'accounts/payment.html')

# def paymentSuccess(request):
#     return redirect('orders')

# def paymentCancel(request):
#     return redirect('orders')



# endpoint_secret = settings.STRIPE_WEBHOOK_KEY

# @csrf_exempt
# def my_webhook_view(request):

#     # stripe listen --forward-to http://127.0.0.1:8000/webhook/stripe/

#     print("in webhook")
#     payload = request.body
#     # print(payload)
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#         payload, sig_header, endpoint_secret)
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)


#   # Handle the checkout.session.completed event
#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']

#     print("before paid")
#     print(session)
#     if session.payment_status == "paid":
#         print("in paid")
#         # Fulfill the purchase...
#         line_item = session.list_line_items(session.id,limit = 1).data[0]
#         order_id = line_item['description']
#         print("before fulfil")
#         fulfill_order(order_id,session)

#   # Passed signature verification
#     return HttpResponse(status=200)


# def fulfill_order(order_id,session):
#     print("Fulfilling order")
#     print(order_id)
#     order = OrderPlaced.objects.get(id=order_id)
#     order.payment_id = session.payment_intent
#     order.payment_status = session.payment_status
#     order.save()

def quotepayment(request,id):
    
 cq = Quote.objects.filter(id=id)    
 return render (request,'accounts/quotepayment.html',{'cq':cq})

def quotepaynow(request,id):
 
 cp = Quote.objects.filter(id=id)
 global uuio
 uuio = str(uuid.uuid1())
 uuio = uuio[:6]
 return render(request,'accounts/quotepaynow.html',{'cp':cp,'uuio':uuio})

def Assign_product_to_user(request,id):

    All_user = User.objects.raw("select * from auth_user where is_superuser = 0 and is_staff = 0") 
    Assigned_users = User.objects.raw("select auth_user.id, auth_user.username from accounts_assign_products join auth_user on accounts_assign_products.user_id =  auth_user.id") 
    sub_product = SubProduct.objects.get(id=id) 
    
    


    if request.method == "POST":
        user_id = request.POST['Assign']
        # SubProduct.objects.filter(id=id).update(Assign=Assign)
        print(user_id)
        assign_products.objects.create(user_id=user_id, product_id = id)

        return redirect('adminsubproductlist')
    return render(request,'devadmin/Assign_product_to_user.html',{"All_user":All_user, "Assigned_users": Assigned_users, "Product":sub_product})



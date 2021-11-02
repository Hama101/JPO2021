from django.shortcuts import render , redirect
from . models import Profile
from .QRS import get_img
from django.contrib import messages

from django.conf import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import os
# Create your views here.



def index(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles,
    }
    return render(request, 'index.html' , context)


def profile(request , CIN):
    profile = Profile.objects.get(CIN = CIN)
    context ={
        "profile" : profile,
    }
    return render(request, 'profile.html' , context)

#create_profile
def create_profile(request):
    
    if request.method == 'POST':
        profile = Profile()
        try : 
            profile.name = request.POST.get('name')
            profile.CIN = request.POST.get('CIN')
            profile.email = request.POST.get('email')
            profile.description = request.POST.get('description')
            profile.title = request.POST.get('title')
            profile.facebook = request.POST.get('facebook')
            profile.linkedin = request.POST.get('linkedin')
            profile.fac = request.POST.get('fac')
            profile.phone = request.POST.get('phone')
            profile.face = request.FILES.get('face')
            
            profile.save()
            print('Profile created : ', profile)
            
            
            
            # configure your email address
            # step1:
            email_user = 'hmdmohamed123@gmail.com'
            email_password = 'zjvkflnhmqlykugy'
            email_send = profile.email

            # step2:
            # https://myaccount.google.com/lesssecureapps
            # Allow less secure apps: ON (remember you must be on for sending email)

            subject = 'JPO 2021 ticket'
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            msg.attach(MIMEText('<html><body>' + "<h2> Please save this QR code !</h2>", 'html', 'utf-8'))

            # configure your own file path
            filename = get_img(profile.CIN)
            attachment = open(filename,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)
            server.sendmail(email_user,email_send,text)
            server.quit()
            
            messages.success(request , f"Welcome, please check you mail!")
            
            if os.path.exists(filename):
                os.remove(filename)
            
            return redirect('profile' , CIN = profile.CIN)
        except Exception as e:
            print(e)
            messages.error(request , f"Error : {e}")
            
    
    return render(request, 'create_profile.html')
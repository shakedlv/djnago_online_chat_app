from asyncore import write
from csv import writer
from operator import le
from django.http import HttpResponseRedirect
from django.utils.timezone import datetime
from django.shortcuts import redirect, render
import string
import random
from main import models 

def home(request):
     context = {}

     if 'usercode' in request.session:
          if 'usergentime' in request.session:
               usergentime = request.session['usergentime']
               lastdate = datetime.strptime(usergentime, '%m/%d/%Y, %H:%M:%S')
               if (datetime.now() - lastdate).total_seconds() >= 1800:
                    request.session['usercode'] = str(random.randint(0, 9)) +  ''.join(random.choice(string.ascii_uppercase) for i in range(2))
                    request.session['usergentime'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    usercode =  request.session['usercode']
               else:
                    usercode =  request.session['usercode']
          else:
               request.session['usercode'] = str(random.randint(0, 9)) +  ''.join(random.choice(string.ascii_uppercase) for i in range(2))
               request.session['usergentime'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
               usercode =  request.session['usercode']
     else:
          request.session['usercode'] = str(random.randint(0, 9)) +  ''.join(random.choice(string.ascii_uppercase) for i in range(2))
          request.session['usergentime'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
          usercode =  request.session['usercode']

     context["usercode"] = usercode

     return render(request, "main/home.html", context)

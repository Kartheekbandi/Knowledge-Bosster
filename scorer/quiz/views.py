from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Questions,MATQuestions,GKQuestions
from django.contrib.auth.models import User,auth
from accounts.models import UserDetails
import time
import random
# Create your views here.
def questions(request):
    ques = Questions.objects.all()
    list=random.sample(range(0, 9), 5)
    ques1=[]
    for i in list:
       ques1.append(ques[i])
    if request.method == 'POST':
         result=request.POST.get('myField')
         res=result.split('$')
         totalscore=len(res)
         count=0
         for i in range(0,totalscore-1):
               if ques[i].answer == res[i]:
                     count=count+1
         current_user = request.user 
         usermarks = UserDetails.objects.filter(user_id = current_user.id).update(enmarbe=count)
         examtime= UserDetails.objects.filter(user_id = current_user.id).update(examtime=time.strftime("%H"))
         totalscore=totalscore-1
         return render(request,'results.html',{'score':count , 'totalscore':totalscore})
    else:
         return render(request,'quiz.html',{'ques':ques1})

def matquestions(request):
    ques = MATQuestions.objects.all()
    list=random.sample(range(0,9), 5)
    ques1=[]
    for i in list:
       ques1.append(ques[i])
    if request.method == 'POST':
         result=request.POST.get('myField')
         res=result.split('$')
         totalscore=len(res)
         count=0
         for i in range(0,totalscore-1):
               if ques[i].answer == res[i]:
                     count=count+1
         current_user = request.user 
         usermarks = UserDetails.objects.filter(user_id = current_user.id).update(enmarbe=count)
         examtime= UserDetails.objects.filter(user_id = current_user.id).update(mattime=time.strftime("%H"))
         totalscore=totalscore-1
         return render(request,'results.html',{'score':count , 'totalscore':totalscore})
    else:
         return render(request,'quiz.html',{'ques':ques1})

def gkquestions(request):
    ques = GKQuestions.objects.all()
    list=random.sample(range(0, 9), 5)
    ques1=[]
    for i in list:
       ques1.append(ques[i])
    if request.method == 'POST':
         result=request.POST.get('myField')
         res=result.split('$')
         totalscore=len(res)
         count=0
         for i in range(0,totalscore-1):
               if ques[i].answer == res[i]:
                     count=count+1
         current_user = request.user 
         usermarks = UserDetails.objects.filter(user_id = current_user.id).update(gkmarks=count)
         examtime= UserDetails.objects.filter(user_id = current_user.id).update(gktime=time.strftime("%H"))
         totalscore=totalscore-1
         return render(request,'results.html',{'score':count , 'totalscore':totalscore})
    else:
         return render(request,'quiz.html',{'ques':ques1})
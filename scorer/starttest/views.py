from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from accounts.models import UserDetails
import time
# Create your views here.
def begintest(request):
    current_user=request.user
    examti = UserDetails.objects.filter(user_id = current_user.id).values('examtime')[0]
    exam=examti['examtime']
    examtimat = UserDetails.objects.filter(user_id = current_user.id).values('mattime')[0]
    exammat=examtimat['mattime']
    present=int(time.strftime("%H"))
    examtigk = UserDetails.objects.filter(user_id = current_user.id).values('gktime')[0]
    examgk=examtigk['gktime']
    present=int(time.strftime("%H"))
    timediff=0
    timediffmat=0
    timediffgk=0
    print(type(exam))
    print(type(exammat))
    print(type(examgk))
    print(exam-present)
    print(exammat-present)
    if exam-present>12:
        timediff=1
    else:
        timediff=0

    if exammat-present>12:
        timediffmat=1
    else:
        timediffmat=0

    if examgk-present>12:
        timediffgk=1
    else:
        timediffgkt=0
    
    return render(request,'starttest.html',{'timediff':timediff,'timediffmat':timediffmat,'timediffgk':timediffgk})
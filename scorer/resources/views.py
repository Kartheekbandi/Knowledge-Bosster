from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from accounts.models import UserDetails
import time
# Create your views here.
def english(request):
    return render(request,'resources.html')
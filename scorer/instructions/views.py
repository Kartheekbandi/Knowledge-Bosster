from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from accounts.models import UserDetails
import time
# Create your views here.
def instructions(request):
    return render(request,'instructions.html')
def instructionsmat(request):
    return render(request,'instructionsmat.html')
def instructionsgk(request):
    return render(request,'instructionsgk.html')
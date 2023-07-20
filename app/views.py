from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFOD=UserForm(request.POST)
        PFOD=ProfileForm(request.POST,request.FILES)
        if UFOD.is_valid() and PFOD.is_valid():
            NSUFO=UFOD.save(commit=False)
            SubmittedPassword=UFOD.cleaned_data['password']
            NSUFO.set_password(SubmittedPassword)
            NSUFO.save()
            NSPFO=PFOD.save(commit=False)
            NSPFO.username=NSUFO
            NSPFO.save()
            return HttpResponse('registration is successful')
    return render(request,'registration.html',d)
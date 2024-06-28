from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from operator import index
from .models import values

# Create your views here.
#index
def index(request):
          return render(request, 'index.html')
#about
def about(request):
        return render(request, 'about.html')

#contact
def contact(request):
    if request.method == 'POST':
        Fname = request.POST.get('Fname')
        Lname = request.POST.get('Lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        values.objects.create(Fname=Fname, Lname=Lname, email=email, message=message)

        return redirect('success')  
    else:
        return render(request, 'contact.html')
#success
def success(request):
       return render(request, 'success.html')
#profile
def profile(request):
        return render(request, 'profile.html')

#management
def management(request):
        return render(request, 'management.html')

#Financial crime
def fcrime(request):
        return render(request, 'financial.html')

#license
def license(request):
        return render(request, 'license.html')

#TFA
def tf(request):
        return render(request, 'tradefinance.html')

#BG
def bg(request):
        return render(request, 'bankguarantee.html')

#SLC
def slc(request):
        return render(request, 'standbyletterofcredit.html')

#dlc
def dlc(request):
        return render(request, 'documentaryletterofcredit.html')

#POF
def pof(request):
        return render(request, 'proofoffunds.html')

#FACS
def facs(request):
        return render(request, 'financialadvisory.html')

#CFA
def cfa(request):
        return render(request, 'cfa.html')
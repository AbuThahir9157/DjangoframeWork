from django.shortcuts import render

from django.http import HttpResponse
from .models import Department,Doctors
from .forms import Bookingform

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    form=Bookingform()
    dict_form={
        'form': form
    }
    return render(request,dict_form,'booking.html')
def doctor(request):
    dict_doc ={
        'doctors':Doctors.objects.all()
    }

    return render(request,'doctor.html',dict_doc)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept': Department.objects.all()
    }
    return render(request,'department.html',dict_dept)
def details(request):
    return render(request,'Details.html')











from django.shortcuts import render
from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from datetime import datetime
import time
from django.db import connection


#Login Page
def login(request):
  return render(request, 'login.html')

#Admin: Department

def admin_department(request):
  return render(request, 'admin_department.html')

#Admin: Doctor
def admin_doctor(request):
  return render(request, 'admin_doctor.html')

#Admin: Nurse
def admin_nurse(request):
  return render(request, 'admin_nurse.html')

#Admin: Medication
def admin_medicine(request):
  return render(request, 'admin_medicine.html')


#Doctor: Add delivery jobs (NEW)
def doctor_emr(request):
  return render(request, 'doctor_emr.html')


#Doctor: Past records
def doctor_history(request):
  return render(request, 'doctor_history.html')


#Nurse: Home
def nurse_home(request):    
  return render(request, 'nurse_home.html')



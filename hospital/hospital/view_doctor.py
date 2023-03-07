from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from datetime import datetime
import time
from django.db import connection

@api_view(['GET',"POST"])
# Doctor/Pharmacist Log In
def doctorLogin(request):
  id_card = request.POST.get('name')
  password = request.POST.get('password')
  # Verifies log in details against database
  user = user_doctor.objects.filter(id_card=id_card).first()
  if not user:
    # If user does not exist, it returns the message
    return Action.fail("User does not exist.")
  if user.password != password:
    # If user does not exist, password incorrect, it will return this message
    return Action.fail("Password Incorrect")
  # Successful Log In
  # return render(request, 'admin.html')
  return Action.success(UserDoctorSerializer(user, many = False).data)

@api_view(['GET',"POST"])
# Doctor's list
def doctorList(request):
  list = user_doctor.objects.all()
  arr = []
  for item in list:
    temp = {}
    temp['id'] = item.id
    temp['name'] = item.name
    temp['id_card'] = item.id_card
    temp['department_id'] = item.department_id
    temp['department_name'] = department.objects.filter(id=item.department_id).first().name
    # temp['password'] = item.password
    # temp['status'] = item.status
    arr.append(temp)
  # Successful log in
  return Action.success(arr)

@api_view(['GET',"POST"])
# Add more doctors/ pharmacist
def doctorAdd(request):
  name = request.POST.get('name')
  id_card = request.POST.get('id_card')
  department_id = request.POST.get('department_id')
  password = request.POST.get('password')
  # Checks if identity already exists 
  sameIdCardUserList = user_doctor.objects.filter(id_card=id_card)
  if sameIdCardUserList.exists() == True :
    # If identity already exists, it returns the following
    return Action.fail("User already exists!")
  # Else, identity is added to the database
  doctor = user_doctor(name=name, id_card=id_card, department_id=department_id, password=password)
  doctor.save()
  # Added successfully
  return Action.success()

'''
@api_view(['GET',"POST"])
# Status tracking of medications with delivery not completed yet
def deliveryList(request):
  list = user_patient.objects.all()
  arr = []
  for item in list:
    temp = {}
    if item.status == "Pending":
      temp["patient_id"] = item.patient_id
      temp["ward_number"] = item.ward_number
      temp["status"] = item.status
      temp["recorded_date"] = item.recorded_date
      temp["recorded_time"] = item.recorded_time

      arr.append(temp)
  return Action.success(arr)
'''
'''
@api_view(['GET',"POST"])
def deliveryJob(request):
    patient_id = request.POST.get('patient_id')
    ward_number = request.POST.get('ward_number')
    status = request.POST.get('status')
    assigned_by = request.POST.get('assigned_by')
    received_by = request.POST.get('received_by')
    recorded_date = datetime.now().date().strftime('%Y-%m-%d')
    recorded_time = time.strftime("%H:%M:%S", time.localtime())

    # Verifies patient ID against database
    existing_patient = patients_data.objects.filter(patient_id=patient_id)
    if existing_patient.exists() == False:
        return Action.fail("Patient don't exist!")
    
    c = connection.cursor()
    c.execute("INSERT INTO user_patient (patient_id, ward_number, status, assigned_by, received_by, recorded_date, recorded_time) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(patient_id, ward_number, status, assigned_by, received_by, recorded_date, recorded_time))
    
    # To add: Since there is a new order, I check the database to count if there are 6 boxes/ 15 mins interval
    # Trigger robot to arrive

    
    return Action.success()
'''

################################## doctor_emr.html #########################################
@api_view(['GET',"POST"])
# EMR Records
def emrList(request):
  list = patients_data.objects.all()
  arr = []
  for item in list:
    temp = {}
    temp["id"] = item.id
    temp["order_id"] = item.order_id
    temp["ward_number"] = item.ward_number
    arr.append(temp)

  return Action.success(arr)


@api_view(['GET',"POST"])
def medicineRequestSelect(request):
  
  id = request.POST.get('id')
  order_id = request.POST.get('order_id')
  ward_number = request.POST.get('ward_number')
  print("Values: ", id, order_id, ward_number)

  updated_list = patients_data.objects.all()
  # Drop that specific row

  # updated_list.save()
  
  #if request.method == 'POST':
    #print("Got it!")
  return Action.success()




    
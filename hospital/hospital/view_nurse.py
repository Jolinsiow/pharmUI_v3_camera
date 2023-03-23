from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from datetime import datetime
import time
from django.db import connection
import json


@api_view(['GET',"POST"])
# Nurse Log In
def nurseLogin(request):
  id_card = request.POST.get('name')
  password = request.POST.get('password')
  # Verifies log in details against database
  user = user_nurse.objects.filter(id_card=id_card).first()
  if not user:
    # If user does not exist, it returns the message
    return Action.fail("User does not exist.")
  if user.password != password:
    # If user does not exist, password incorrect, it will return this message
    return Action.fail("Password Incorrect")
  
  # Successful Log In
  c = connection.cursor()
  c.execute("INSERT INTO nurselogin (id_card) VALUES ('{0}');".format(id_card))
  return Action.success(UserNurseSerializer(user, many = False).data)


@api_view(['GET',"POST"])
# Nurse's list
def nurseList(request):
  list = user_nurse.objects.all()
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
# Add more nurse
def nurseAdd(request):
  name = request.POST.get('name')
  id_card = request.POST.get('id_card')
  department_id = request.POST.get('department_id')
  password = request.POST.get('password')
  # Checks if identity already exists 
  sameIdCardUserList = user_nurse.objects.filter(id_card=id_card)
  if sameIdCardUserList.exists() == True :
    # If identity already exists, it returns the following
    return Action.fail("User already exists!")
  # Else, identity is added to the database
  nurse = user_nurse(name=name, id_card=id_card, department_id=department_id, password=password)
  nurse.save()
  # Added successfully
  return Action.success()

# from .robot_prompt import countdown  # Calling external python file: robot_prompt (TEST)

@api_view(['GET',"POST"])
def nurse_qrscan(request):
  if request.method == 'POST':
    # parse the JSON data
    data = json.load(request)
    result = data.get("result")
    
    if result != None:
      c = connection.cursor()
      # Saving the result to database, nurse_QR
      c.execute("INSERT INTO nurse_QR (output) VALUES ('{0}');".format(result)) # Not needed anymore

      # Status update to "Retrieved"
      # Add in "received_by" after nurse scans QR code to acknowledge receipt of medications
      c.execute("SELECT id_card FROM nurselogin")
      received_by = c.fetchall()[-1][0]  
      c.execute("UPDATE user_patient SET status='Retrieved' WHERE box_number = '%s'" % (result)) 
      c.execute("UPDATE user_patient SET received_by='%s' WHERE box_number = '%s'" % (received_by, result)) 
      
      return Action.success()



    

 
    





    
  
    
  
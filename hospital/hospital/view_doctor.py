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
  c = connection.cursor()
  c.execute("INSERT INTO pharmacistlogin (id_card) VALUES ('{0}');".format(id_card))
  
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



from django.views.decorators.csrf import csrf_exempt

@api_view(['GET',"POST"])
@csrf_exempt
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


import json
from django.http import JsonResponse
from .timer import TimerClass


@api_view(['GET',"POST"])
def medicineRequestSelect(request):
  if request.method == 'POST':
    data = json.loads(request.body.decode('utf-8'))
    qr_code = data.get('qr_code')
    row_data = data.get('row_data')

    id = row_data['id']
    order_id = row_data['order_id']
    ward_number = row_data['ward_number']
    box_number = qr_code
    status = "Pending"
    recorded_date = datetime.now().date().strftime('%Y-%m-%d')
    recorded_time = time.strftime("%H:%M:%S", time.localtime())
   
    c = connection.cursor()
    c.execute("SELECT id_card FROM pharmacistlogin")
    assigned_by = c.fetchall()[-1][0]  

    c.execute("INSERT INTO user_patient (order_id, box_number, ward_number, status, recorded_date, recorded_time, assigned_by) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(order_id, box_number, ward_number, status, recorded_date, recorded_time, assigned_by))

    # Connect to EMR to drop that row! Update OrderIDList
    order_id_str = str(order_id)
    c.execute("DELETE FROM patients_data WHERE order_id = '%s'" % (order_id_str))


    ####################### ROBOT PROMPT TRIGGER #############################
    # To add: Since there is a new order, I check the database to count if there are 6 boxes/ 15 mins interval
    c.execute("SELECT COUNT(*) FROM user_patient WHERE status = '%s'" % ("Pending"))  
    for record in c.fetchall():     
        tmr = TimerClass()
        
        if record[0] == 1:
          print("There is only 1 Pending box in the database")
          tmr.start()    
          # For demo purpose: As long as there is 1 "Pending" box, ACTIVATE ROBOT
            
          
        elif record[0] == 6 and tmr.count != 0: # There are already 6 boxes and timer function has not ended, stop the timer and call the robot
          tmr.stop()
          print("There are already 6 boxes but timer is not up. Stop timer function and call the robot")
          
          # Write robot_prompt into the DB to send to REST Server / Link to call robot
          robot_prompt = "Activate"
          c.execute("INSERT INTO robot_prompt (robot_prompt) VALUES ('{0}');".format(robot_prompt))
          
        
        elif record[0] == 7:
          print("Loop restart")
  
          tmr.start()

        else:
          continue

    return JsonResponse({'success': True})
  else:
    return JsonResponse({'success': False, 'message': 'Invalid request method'})
  

# doctor_deliverylist.html

@api_view(['GET',"POST"])
# Status tracking of medications with delivery not completed yet
def deliveryList(request):
  list = user_patient.objects.all()
  arr = []
  for item in list:
    temp = {}
    if item.status != "Completed":   # Actually, this line is redundant now since all "Completed" ones will be in past_history table
      temp["job_id"] = item.job_id
      temp["order_id"] = item.order_id
      temp["ward_number"] = item.ward_number
      temp["status"] = item.status
      temp["recorded_date"] = item.recorded_date
      temp["recorded_time"] = item.recorded_time

      arr.append(temp)
  return Action.success(arr)

      


    
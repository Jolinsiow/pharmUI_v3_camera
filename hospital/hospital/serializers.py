from rest_framework import serializers
from .models import *


# 对数据进行序列化
# Admin Data
class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = admin
        fields = ['id', 'name', 'password']

# Doctor/Pharmacist Data
class UserDoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_doctor
        fields = ['id', 'name', 'id_card', 'department_id', 'password', 'status']

# Nurse Data
class UserNurseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_nurse
        fields = ['id', 'name', 'id_card', 'department_id', 'password', 'status']

# Department Data
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = department
        fields = ['id', 'name', 'registration_fee', 'doctor_num']

# Medication Data
class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = medicine
        fields = ['id', 'name', 'price', 'unit']



# New medication delivery job
class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_patient
        fields = ['id', 'job_id', 'order_id', 'box_number', 'ward_number', 'status', 'recorded_date', 'recorded_time', 'slot_number', 'assigned_by', 'received_by']


# Mimic CPS
class CPSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patients_data
        fields = ['id', 'order_id', 'ward_number']


#### Date
class DATESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test_date
        fields = ['id', 'select_date']

#### To record robot prompt
class RobotPromptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = robot_prompt
        fields = ['robot_prompt']


#### Nurse QR
class NurseQRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = nurse_QR
        fields = ['id', 'output']

### Personal: To record pharmacist login
class PharmLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pharmacistlogin
        fields = ['id_card']

### Personal: To record nurse login
class NurseLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = nurselogin
        fields = ['id_card']

##### Pharmacist portal: Past Records 
class PastRecordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = past_records
        fields = ['id', 'job_id', 'order_id', 'ward_number', 'status', 'recorded_date', 'recorded_time', 'assigned_by', 'received_by']


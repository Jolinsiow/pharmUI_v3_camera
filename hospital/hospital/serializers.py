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
        fields = ['id', 'job_id', 'order_id', 'box_number', 'ward_number', 'status', 'recorded_date', 'recorded_time', 'slot_number']


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


#### Can delete
class NurseQRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = nurse_QR
        fields = ['id', 'output']
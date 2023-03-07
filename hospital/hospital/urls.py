"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from hospital import view_admin
from hospital import view_doctor
from hospital import view_nurse
from hospital import view_medicine
from hospital import view_department
from hospital import view_doctor_history
from django.urls import path
from . import views

urlpatterns = [
    # Main Page
    path('', views.login, name='login'),
    path('login/', views.login),
    path('admin/', views.admin_department, name='admin_department'),
    path('admin_department/', views.admin_department),
    path('admin_doctor/', views.admin_doctor),
    path('admin_nurse/', views.admin_nurse),
    path('admin_medicine/', views.admin_medicine),

    path('doctor/', views.doctor_history),
    path('doctor_history/', views.doctor_history),

    path('doctor_emr/', views.doctor_emr), 

    path('nurse/', views.nurse_home),
    path('nurse_home/', views.nurse_home),

    # Data Request

    # Admin
    path('adminLogin', view_admin.adminLogin, name='adminLogin'),
    path('departmentList', view_department.departmentList, name='departmentList'),
    path('doctorList', view_doctor.doctorList, name='doctorList'),
    path('doctorAdd', view_doctor.doctorAdd, name='doctorAdd'),
    path('nurseList', view_nurse.nurseList, name='nurseList'),
    path('nurseAdd', view_nurse.nurseAdd, name='nurseAdd'),

    # Medicine
    path('medicineList', view_medicine.medicineList, name='medicineList'),
    path('medicineStrList', view_medicine.medicineStrList, name='medicineStrList'),
    path('medicineAdd', view_medicine.medicineAdd, name='medicineAdd'),

    # Nurse
    path('nurseLogin', view_nurse.nurseLogin, name='nurseLogin'),
    path('nurse_qrscan', view_nurse.nurse_qrscan, name='nurse_qrscan'),

    # Doctor
    path('doctorLogin', view_doctor.doctorLogin, name='doctorLogin'),
    #path('deliveryJob', view_doctor.deliveryJob, name="deliveryJob"),
    path('emrList', view_doctor.emrList, name='emrList'),
    path('medicineRequestSelect', view_doctor.medicineRequestSelect, name='medicineRequestSelect'),
    #path('deliveryList', view_doctor.deliveryList, name="deliveryList"),
    path('historyList', view_doctor_history.historyList, name="historyList"),
    path('onSearchDate', view_doctor_history.onSearchDate, name="onSearchDate"),
]

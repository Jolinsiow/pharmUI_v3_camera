from django.contrib import admin

from hospital.models import user_patient
from hospital.models import past_records
from hospital.models import patients_data
# Register your models here.

admin.site.register(patients_data)
admin.site.register(user_patient)
admin.site.register(past_records)

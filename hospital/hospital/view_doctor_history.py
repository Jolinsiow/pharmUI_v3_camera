from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from datetime import datetime
from django.db import connection



@api_view(['GET',"POST"])
def onSearchDate(request):
    select_date = request.POST.get("select_date")
    c = connection.cursor()
    c.execute("INSERT INTO test_date (select_date) VALUES ('{0}');".format(select_date))

    return Action.success()


# Retrieve past records based on date filtered
# (Note: In DB, I populated test_date with some dates, otherwise when test_date table is empty, it will have Internal Error: NoneType )

@api_view(['GET',"POST"])
def historyList(request):
    list = past_records.objects.all()
    arr = []
    c = connection.cursor()
    c.execute("SELECT u.select_date FROM test_date u")
    date_selected = c.fetchall()[-1][-1]   
    for item in list:
        temp = {}
        if item.recorded_date == date_selected:
            temp["id"] = item.id
            temp["job_id"] = item.job_id
            temp["order_id"] = item.order_id
            temp["ward_number"] = item.ward_number
            temp["status"] = item.status
            temp["recorded_date"] = item.recorded_date
            temp["recorded_time"] = item.recorded_time
            temp["assigned_by"] = item.assigned_by
            temp["received_by"] = item.received_by

            arr.append(temp)

    return Action.success(arr)




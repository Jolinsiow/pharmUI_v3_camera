from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
import logging

def custom_exception_handler(exc, context):
    """
    :param exc: Suggestion to handle error
    :param context:  Returns error text
    :return: Response
    """
    response = exception_handler(exc, context)
    if response is None:
        print(exc)

    return Response({"code":500, "data": 'Internal Server Error'})
from django.shortcuts import render
from django.http import HttpResponse


def submit_expenses(request):
    """ User submits an expense"""
    return HttpResponse("Hello World")

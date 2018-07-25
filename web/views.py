from django.shortcuts import render
from django.http import HttpResponse
from .models import Token, Expense, User, Income
from datetime import datetime
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_expenses(request):
    """  User submits an expense """
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_incomes(request):
    """  User submits an expense """
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Income.objects.create(user=this_user, amount=request.POST['amount'],
                          text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)

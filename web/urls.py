from django.urls import path, re_path
from . import views

urlpatterns = [
    path('submit/expenses/', views.submit_expenses, name='submit_expenses')
]

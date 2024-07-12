from django.shortcuts import redirect,render
from django.contrib import messages
from django.http import HttpResponse


def employee_dashboard (request):
    return HttpResponse ("<h1>Welcome employee</h1>")
    #return render ('emoloyee_dashboard.html')

from django.shortcuts import redirect,render
from django.contrib import messages
from django.http import HttpResponse


def admin_dashboard (request):
    # return HttpResponse ("<h1>Welcome admin</h1>")
    return render (request,'admin_page/admin_dashboard.html')

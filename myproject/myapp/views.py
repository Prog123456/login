from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def login (request):
    return render (request ,'login.html')

def dologin (request):
    
    if request.method == "POST":
        username = request.POST.get('employee_ID')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            if user.is_superuser:
                login(request)
                # return HttpResponse('<h2>welcome admin</h2>')
                return redirect ('admin_dashboard')
            else:
                login(request)
                # return HttpResponse('<h2>welcome employee</h2>')
                return redirect ('employee_dashboard')
        else:
            # return HttpResponse('<h2>welcome</h2>')
            messages.error(request, "Invalid Email or Password.")
            return render(request, 'login.html', {'error_message': 'Invalid Login'})
    else:
        messages.error(request, 'Invalid Login Credentials !')
        return redirect(request,'login.html')

        

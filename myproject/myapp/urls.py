from django.urls import path
from . import views,AdminViews,EmployeeViews

urlpatterns = [
    path('',views.login, name = 'login'),
    path('dologin/',views.dologin, name = 'dologin'),

    #===========Admin===========#

    path('admin_dashboard/', AdminViews.admin_dashboard,name = "admin_dashboard")
]

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):


 model = User
 list_display = ('username', 'email', 'is_admin', 'is_employee')
 list_filter = ('is_admin', 'is_employee')
 fieldsets = ( (None, {'fields': ('username', 'password')}), ('Personal info', {'fields': ('first_name', 'last_name', 'email')}), ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_employee')}), ('Important dates', {'fields': ('last_login', 'date_joined')}), )


admin.site.register(User, CustomUserAdmin)

from django.contrib import admin

from core.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'department']


admin.site.register(Employee, EmployeeAdmin)

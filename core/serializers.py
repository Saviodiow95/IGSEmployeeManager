from rest_framework import serializers

from core.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class EmployeeReadOnlySerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']
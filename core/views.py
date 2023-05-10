from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from core.models import Department, Employee
from core.serializers import DepartmentSerializer, EmployeeRegistrationSerializer, EmployeeReadOnlySerializer


class HomeView(TemplateView):
    departments = Department.objects.all()
    employees = Employee.objects.all()

    extra_context = {'departments': departments, 'employees': employees}

    template_name = 'core/home.html'


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = LimitOffsetPagination


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method.upper() == "GET":
            return EmployeeReadOnlySerializer
        return EmployeeRegistrationSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method.upper() == "GET":
            return EmployeeReadOnlySerializer
        return EmployeeRegistrationSerializer

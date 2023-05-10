from django.urls import path

from core.views import HomeView, DepartmentList, DepartmentDetail, EmployeeList, EmployeeDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('department/', DepartmentList.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
]

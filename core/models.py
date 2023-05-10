from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='name', max_length=50, blank=False, null=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(verbose_name='name', max_length=250, blank=False, null=False)
    email = models.EmailField(verbose_name='email', blank=False, null=False)
    department = models.ForeignKey(Department, verbose_name='department', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

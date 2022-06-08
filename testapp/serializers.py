
from django.db.models import fields
from testapp import views

from rest_framework import serializers
from testapp.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
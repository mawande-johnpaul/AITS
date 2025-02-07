from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','student_number']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name','administrator']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['sender','date','summary','description', 'attachments']
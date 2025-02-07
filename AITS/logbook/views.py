from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UserView(APIView):
    def get(self, request):
        output = [{'first_name': output.first_name, 'last_name':output.last_name, 'email':output.email, 'student_number':output.student_number}
        for output in User.objects.all()]

        return Response(output)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class DepartmentView(APIView):
    def get(self, request):
        output = [{'name': output.name, 'administrator':output.administrator}
        for output in User.objects.all()]

        return Response(output)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class IssueView(APIView):
    def get(self, request):
        output = [{'sender': output.sender, 'date':output.date, 'summary':output.summary, 'description':output.description, 'attachments':output.attachments}
        for output in User.objects.all()]

        return Response(output)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

def dashboard(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        return JsonResponse({"status": "success", "message": f"Welcome, {email}!{password}"})
def signup(request):
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    email = request.POST['email']
    student_number = request.POST['student-number']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    return render(request, 'login.html')

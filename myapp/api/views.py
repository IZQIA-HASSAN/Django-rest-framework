from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Stu_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id' , None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = Stu_serializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type = "applicatoin/json")

        stu = Student.objects.all()
        serializer = Stu_serializer(stu , many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data , content_type = 'application/json')



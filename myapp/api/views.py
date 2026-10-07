from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Stu_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views import views


# this is the class based view for same function

# @method_decorator(csrf_exempt , name='dispatch')
# class Studentapi(view):
#     def get(self , request , *args , **kwargs):
#         if request.method == "GET":
#                 json_data = request.body
#                 stream = io.BytesIO(json_data)
#                 python_data = JSONParser().parse(stream)
#                 id = python_data.get('id' , None)
#                 if id is not None:
#                     stu = Student.objects.get(id = id)
#                     serializer = Stu_serializer(stu)
#                     json_data = JSONRenderer().render(serializer.data)
#                     return HttpResponse(json_data , content_type = "applicatoin/json")
        
#                 stu = Student.objects.all()
#                 serializer = Stu_serializer(stu , many=True)
#                 json_data = JSONRenderer().render(serializer.data)
#                 return HttpResponse(json_data , content_type = 'application/json')



@csrf_exempt
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

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = Stu_serializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type = "application/json")

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        stu = Student.objects.get(id=id )
        serializer = Stu_serializer(stu , data=python_data , partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : "Data updated sucessfully !"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type="application/json")

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'mes' : "seccuessfully deleted"}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data , content_type="application/json")
        # these two lines can be replaced by this line below
        return JsonResponse(res , safe=False)





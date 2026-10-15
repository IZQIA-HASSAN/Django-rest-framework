# # from django.shortcuts import render
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import Student
# # from .serializer import StudentSerializer
# # from rest_framework import status
# # from rest_framework.views import APIView\

# # class StudentAPI(APIView):
# #     def get(self , request , format=None ,pk=None):
        
# #                 id = pk
# #                 if id is not None:
# #                     stu = Student.objects.get(id=id)
# #                     serializer = StudentSerializer(stu)
# #                     return Response(serializer.data)
# #                 stu = Student.objects.all()
# #                 serializer = StudentSerializer(stu , many=True)
# #                 return Response(serializer.data)

# #     def post(self , request , format=None):
# #          serializer = StudentSerializer(data = request.data)
# #          if serializer.is_valid():
# #             serializer.save()
# #             return Response({'msg' : 'Data Created'},status=status.HTTP_201_CREATED)
# #          return Response({'msg' : 'Data not created'} , status=status.HTTP_400_BAD_REQUEST )

# #     def put(self , request , format=None , pk=None):
# #         id = pk
# #         stu = Student.objects.get(pk=id)
# #         serializer = StudentSerializer(stu , data=request.data , partial=True)
# #         if serializer.is_valid():
# #           serializer.save()
# #           return Response({'msg' : "Data updated"})
# #         return Response(serializer.errors)

# #     def delete(self , request , format=None , pk=None):
# #         id = pk
# #         if id is not None:
# #          stu = Student.objects.delete(pk=id)
# #          stu.delete()
# #          return Response({'msg' : 'Data deleted'})


         
         
         


# # # # Create your views here.
# # # @api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])

# # # def student_api(request , pk=None ):
# # #     if request.method == 'GET':
# # #         id = pk
# # #         if id is not None:
# # #             stu = Student.objects.get(id=id)
# # #             serializer = StudentSerializer(stu)
# # #             return Response(serializer.data)
# # #         stu = Student.objects.all()
# # #         serializer = StudentSerializer(stu , many=True)
# # #         return Response(serializer.data)

# # #     if request.method == 'POST':
# # #         serializer = StudentSerializer(data = request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response({'msg' : 'Data Created'},status=status.HTTP_201_CREATED)
# # #         return Response({'msg' : 'Data not created'} , status=status.HTTP_400_BAD_REQUEST )

# # #     if request.method == 'PUT':
# # #         id = pk
# # #         stu = Student.objects.get(pk=id)
# # #         serializer = StudentSerializer(stu , data=request.data , partial=True)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response({'msg' : "Data updated"})
# # #         return Response(serializer.errors)

# # #     if request.method == 'DELETE':
# # #         id = pk
# # #         if id is not None:
# # #             stu = Student.objects.delete(pk=id)
# # #             stu.delete()
# # #             return Response({'msg' : 'Data deleted'})
            




# # Generic Api view

# # from .models import Student
# # from .serializer import StudentSerializer
# # from rest_framework.generics import GenericAPIView
# # from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin  , UpdateModelMixin , DestroyModelMixin

# # class StudentList_create(GenericAPIView , ListModelMixin , CreateModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# #     def get(self , request , *args , **kwargs):
# #         return self.list(request , *args , **kwargs)

# #     def post(self , request , *args , **kwargs):
# #         return self.create(request , *args , **kwargs)


# # combined the retrive , update and destroy as they all require 'pk'

# # class StudentRUD(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# #     def get(self , request , *args , **kwargs):
# #         return self.retrieve(request , *args , **kwargs)

# #     def put(self , request , *args , **kwargs):
# #             return self.update(request , *args , **kwargs)

# #     def delete(self , request , *args , **kwargs):
# #         return self.destroy(request , *args , **kwargs)



# # class Studentcreate(GenericAPIView , CreateModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# #     def post(self , request , *args , **kwargs):
# #         return self.create(request , *args , **kwargs)

# # class Studentupd(GenericAPIView , UpdateModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# #     def put(self , request , *args , **kwargs):
# #         return self.update(request , *args , **kwargs)

# # class Studentdel(GenericAPIView , DestroyModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# #     def get(self , request , *args , **kwargs):
# #         return self.destroy(request , *args , **kwargs)



# # Concrete API View Class


# from .models import Student
# from .serializer import StudentSerializer
# from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView 
# from rest_framework.throttling import ScopedRateThrottle


# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstu'

# class Studentcreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystu'

# class studentret(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstu'  

# class Studentupd(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystu'

# class Studentdes(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystu'

# # class StudentLC(ListCreateAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # class StudentRU(RetrieveUpdateAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # class StudentRD(RetrieveDestroyAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # class StudentRUD(RetrieveUpdateDestroyAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # we can also do this whole thing with just two classes
# # class StudentRUD(RetrieveUpdateDestroyAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # class StudentLC(ListCreateAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer


# # Viewsets

# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializer import StudentSerializer
# from rest_framework import status
# from rest_framework import viewsets

# class StudentView(viewsets.ViewSet):
#     def list(self , request):
#         print("*********List*********")
#         print("Basename:" , self.basename)
#         print("Action:" , self.action)
#         print("detail:" , self.detail)
#         print("suffix:" , self.suffix)
#         print("Name:" , self.name)
#         print("Description:" , self.description)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu , many=True)
#         return Response(serializer.data)

#     def retrieve(self , request , pk=None):
#      id = pk
#      if id is not None:
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)

#     def create(self , request):
#        serializer = StudentSerializer(data=request.data)
#        if serializer.is_valid():
#           serializer.save()
#           return Response({'msg' : 'Data created'} , status=status.HTTP_201_CREATED)
#        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    

# from .models import Student
# from .serializer import StudentSerializer
# from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from api.customauth  import customauth
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
# from api.throttling import rate

# # custom permission classes

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle , rate]
    


     
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

class studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city' ,'name']
    




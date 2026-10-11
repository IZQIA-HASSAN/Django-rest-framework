from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg' :'Hello World'})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#      return Response({'msg' :'this is post request'})

@api_view(['POST' , 'GET'])
def hello_world(request):
    if request.method == 'GET':
       return Response({'msg' : 'this is get ,ethod'})

    if request.method == 'POST':
     return Response({'msg' :'this is post request'})
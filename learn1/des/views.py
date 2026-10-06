from django.shortcuts import render
from .serializers import Studentserializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):

    if request.method == 'POST':

        # 1. Get JSON data from request body
        json_data = request.body
        print(json_data)

        # 2. Convert bytes into a stream
        stream = io.BytesIO(json_data)

        # 3. Convert JSON into Python dictionary
        python_data = JSONParser().parse(stream)

        # 4. Give the Python data to serializer
        serial = Studentserializer(data=python_data)

        # 5. Validate the data
        if serial.is_valid():

            # 6. Save data into database
            serial.save()

            # 7. Create response dictionary
            res = {'msg': 'Data created!'}

            # 8. Convert Python dictionary into JSON
            json_data = JSONRenderer().render(res)

            # 9. Send JSON response
            return HttpResponse(
                json_data,
                content_type="application/json"
            )
        else:
            json_data = JSONRenderer().render(serial.errors)
            return HttpResponse(
                            json_data,
                            content_type="application/json"
                        )   
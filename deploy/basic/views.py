from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from basic.models import Registration
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def registration_view(request):
    try:
        if request.method =="POST":
            data = json.loads(request.body)

            print(data)

         

            Registration.objects.create(
                name=data["name"],
                email=data["email"],
                course=data["course"],
                phone=data["phone"]
            )

            return JsonResponse({"status": "success","message":"registration successful"})
        else:
            return JsonResponse({"message": "Invalid request method"})
    except Exception as e:
        print(e)
        return JsonResponse({
            "statuscode": 500,
            "error": str(e)
        })



def get_students(request):
     if request.method=="GET":
         registrations=Registration.objects.values()
         return JsonResponse({
             "registrations":list(registrations)
         })
     return JsonResponse({
         "message":"onlu GET method is allowed"
     })

    
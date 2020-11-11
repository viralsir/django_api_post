from django.shortcuts import render
from .models import course
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"courses/view.html",{
        "courses":course.objects.all()
    })

def courseview(request):
    courses=course.objects.all().values()
    courses_list=list(courses)
    return JsonResponse({"data":courses_list})

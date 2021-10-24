from django.shortcuts import render
import json
from django.http import JsonResponse
from django.http import HttpResponse
from faculty.models import Faculty
# Create your views here.
def faculty_info(request):
    faculty={
        'fno':100,
        'f_name':"Khushboo Trivedi",
        'f_sal':100000,
        'f_city':"Pune"
    }
    resp='<h1>Faulty Number:{}<br>Faculty Name:{}<br>Faculty Salary:{}<br>Faculty City:{}</' \
         'h1>'.format(faculty['fno'],faculty['f_name'],faculty['f_sal'],faculty['f_city'])
    return HttpResponse(resp)

def faculty_info1(request):
    faculty={
        'fno':100,
        'f_name':"Khushboo Trivedi",
        'f_sal':100000,
        'f_city':"Pune"
    }
    json_data=json.dumps(faculty)
    return HttpResponse(json_data,content_type='application/json')

def faculty_info2(request):
    faculty={
        'fno':100,
        'f_name':"Khushboo Trivedi",
        'f_sal':100000,
        'f_city':"Pune"
    }
    return JsonResponse(faculty)


# Create your views here.
def faculty_info_view(request):
    faculty=Faculty.objects.all()
    print(faculty)
    return render(request,'faculty/results.html',{'faculty':faculty})


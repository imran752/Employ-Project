from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # stu = Student.objects.all()
    # stu  = Student.objects.exclude(roll)
    stu = Student.objects.order_by('i')
    # print(stu)
    # print(stu.query)
    return render(request, 'index.html',{'stu':stu})


 
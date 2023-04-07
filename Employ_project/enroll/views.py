from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from django.contrib.auth import authenticate , login
from django.contrib.auth.forms import AuthenticationForm
import csv
from .forms import StudentForm
from django.contrib import messages



def StudentData(request):
    stu = Student.objects.all()

    if request.method == 'POST':
        datef = request.POST['fromdate']
        print(datef)
        datet = request.POST['todate']
        print(datet)
        try:
            stu = Student.objects.filter(date__lte=datet, date__gte=datef)
            print(stu)
        except:
            stu=None
        return render(request,'index.html', {'stu': stu})
    print(stu)
    return render(request,'index.html', {'stu': stu})
  

def User_login(request):
   
        if request.method=='POST':
            fm = AuthenticationForm(request=request , data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pwd  = fm.cleaned_data['password']
                user = authenticate(username=uname , password=pwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/st/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
 


def update_data(request,id):
    if request.method=='POST':
        pi = Student.objects.get(pk=id)
        fm =  StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            messages.success(request, 'update successfull')
            fm.save()
            fm = StudentForm()
    else:
        pi = Student.objects.get(pk=id)
        fm =  StudentForm(request.POST, instance=pi)

    return render(request,'update.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi = Student.objects.get(pk=id)
         
        pi.delete()
        return HttpResponseRedirect('/st/')

# def exportcsv(request):
#     stu = Student.objects.filter()
#     response = HttpResponse('text/csv')
#     response['Content-Disposition'] = 'attachment; filename=attendance.csv'
#     writer = csv.writer(response)
#     writer.writerow(['Student_name', 'date', 'time_in', 'time_out'])
#     studs = stu.values_list('Student_name', 'date', 'time_in', 'time_out')
#     for std in studs:
#         writer.writerow(std)
#     return response



 
        







 
from django.shortcuts import render ,HttpResponseRedirect,HttpResponse
from .models import Student
from django.contrib.auth import authenticate , login
from django.contrib.auth.forms import AuthenticationForm
import csv



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
        return render(request,'csv.html', {'stu': stu})
    print(stu)
    return render(request,'csv.html', {'stu': stu})
  

def User_login(request):
   
        if request.method=='POST':
            fm = AuthenticationForm(request=request , data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pwd  = fm.cleaned_data['password']
                user = authenticate(username=uname , password=pwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
 
 

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



 
        







 
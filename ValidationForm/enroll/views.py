from django.shortcuts import render
from .forms import Student
# Create your views here.

def StudentForm(request):
    if request.method=='POST':
        fm = Student(request.POST)
        if fm.is_valid():
          
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['lname'])
            
    else:
        fm = Student()
    return render(request , 'index.html', {'form':fm})
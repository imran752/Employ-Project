 
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.StudentData, name='home'),
    path('', views.User_login, name='login'),
    # path('csv/', views.exportcsv , name='csv')
    
]

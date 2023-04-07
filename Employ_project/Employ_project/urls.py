 
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('st/', views.StudentData, name='studentdata'),
    path('delete/<int:id>/', views.delete_data , name='delete'),
    path('<int:id>/', views.update_data, name='update'),
    path('', views.User_login, name='login'),
    
    
]
    


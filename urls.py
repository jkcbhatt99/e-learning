from django.urls import path

from . import views

 


app_name = 'main'


urlpatterns = [

    path('', views.index1, name='index1'),
    path('home/', views.home, name = 'home'),
   path('Course/', views.Course , name='Course'),
    path('adminp/', views.adminp , name='adminp'),
     path('register/', views.registerUser , name='register'),
    path('login/', views.loginUser , name='login'),
      path('logout/', views.logoutUser, name = 'logout'),
      path('quiz/', views.quiz , name='quiz'),
   path('assign/', views.assign , name='assign'),
   
 


         ]
from django.urls import path
import views

url_patterns = [
    path('', views.FlightList.as_view()), 
    path('<int:pk>/', views.FlightDetail.as_view()), 

    path('', views.SeatList.as_view()), 
    path('<int:pk>/', views.SeatDetail.as_view()),
     
    path('', views.PassengerList.as_view()), 
    path('<int:pk>/', views.PassengerDetail.as_view()), 
    ]
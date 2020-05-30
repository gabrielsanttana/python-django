from django.urls import path
from api import views

urlpatterns = [
  path('hello-view/', views.HelloAPIView.as_view())
]
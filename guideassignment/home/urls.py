from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("userRegister", views.userRegister, name='userRegister'),
    path("guideRegister", views.guideRegister, name='guideRegister'),
    path("details", views.details, name='details'),
    path("guideList", views.guideList, name='guideLIst')





]

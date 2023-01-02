from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='index'),
    path("login", views.login, name='login'),
    path("userRegister", views.userRegister, name='userRegister'),
    path("guideRegister", views.guideRegister, name='guideRegister'),
    path("details", views.details, name='details'),
    path("guideList", views.guideList, name='guideLIst'),
    path("guideDetails", views.guideDetails, name='guideDetails'),
    path("guideLogin", views.guideLogin, name='guideLogin'),
    path("about", views.about, name='about')







]

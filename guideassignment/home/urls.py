from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='index'),
    path("LoginUser", views.LoginUser, name='login'),
    path("logout", views.LogoutPage, name='logout'),
    path("userRegister", views.userRegister, name='userRegister'),
    path("guideRegister", views.guideRegister, name='guideRegister'),
    path("details", views.details, name='details'),
    path("guideList", views.guideList, name='guideLIst'),
    path("guideDetails", views.guideDetails, name='guideDetails'),
    path("guideLogin", views.guideLogin, name='guideLogin'),
    path("about", views.about, name='about'),
    path("map", views.map, name='map'),
    path("chatbox", views.chatbox, name='chatbox')






]

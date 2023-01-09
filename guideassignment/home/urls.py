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
    path("bhaktapurDetails", views.bhaktapurDetails, name='bhaktapurDetails'),
    path("boudhanathDetails", views.boudhanathDetails, name='boudhanathDetails'),
    path("budhanilkanthaDetails", views.budhanilkanthaDetails,
         name='budhanilkanthaDetails'),
    path("kathmanduDetails", views.kathmanduDetails,
         name='kathmanduDetails'),
    path("pashupatinathDetails", views.pashupatinathDetails,
         name='pashupatinathDetails'),
    path("swayambhunathDetails", views.swayambhunathDetails,
         name='swayambhunathDetails'),
    path("changuDetails", views.changuDetails,
         name='changuDetails'),
    path("freakDetails", views.freakDetails,
         name='freakDetails'),
    path("narayanDetails", views.narayanDetails,
         name='narayanDetails'),
    path("babinaDetails", views.babinaDetails,
         name='babinaDetails'),
    path("jinuDetails", views.jinuDetails,
         name='jinuDetails'),
    path("rijanDetails", views.rijanDetails,
         name='rijanDetails'),
    # path("chatbox", views.chatbox, name='chatbox')






]

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def LoginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")

        # print(username, password)

        # user = User.objects.filter(username=username)
        # if user.count() == 0:

    return render(request, 'login.html')


def userRegister(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if password!=confirmpassword:
            return HttpResponse("Your password does not match")
        else:
            my_user = User.objects.create_user(username, email, password)
            # my_user.is_active = True
            my_user.save()
            return redirect ('login')

    return render(request, 'userRegister.html')


def guideRegister(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        # citizenship = request.POST.get("citizenship")

        if password!=confirmpassword:
            return HttpResponse("Your password does not match")
        else:
            my_user = User.objects.create_user(username, email, password)
            # my_user.is_active = True
            my_user.save()
            return redirect ('login')

    return render(request, 'guideRegister.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def details(request):
    return render(request, 'details.html')


def guideList(request):
    return render(request, 'guideLIst.html')


def guideDetails(request):
    return render(request, 'guideDetails.html')


def guideLogin(request):
    return render(request, 'guideLogin.html')


def about(request):
    return render(request, 'about.html')


def map(request):
    return render(request, 'map.html')


@login_required(login_url='login')
def chatbox(request):
    return render(request, 'chatbox.html')



# def gallery(request):
#     return render(request, 'gallery.html')

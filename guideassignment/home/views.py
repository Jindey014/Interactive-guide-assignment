from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def login(request):
    return render(request, 'login.html')


def userRegister(request):
    return render(request, 'userRegister.html')


def guideRegister(request):
    return render(request, 'guideRegister.html')


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

# def gallery(request):
#     return render(request, 'gallery.html')

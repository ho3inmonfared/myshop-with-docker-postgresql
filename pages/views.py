from django.shortcuts import render

def home(request):
    return render(request,'pages/home.html',{})

def aboutus(request):
    return render(request,'pages/aboutus.html',{})

from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'login.html', {})

def m3(request):
    return render(request, 'm3.html', {})

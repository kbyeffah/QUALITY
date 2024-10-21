from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pc(request):
    return render(request, 'pc.html')

def phone(request):
    return render(request, 'phone.html')


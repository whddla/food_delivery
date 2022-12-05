from django.shortcuts import render,redirect

def index(request):
    return render(request, "index.html")

def cate(request):
    return render(request, "cate.html")
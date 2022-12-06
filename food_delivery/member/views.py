from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from food_delivery.models import User
from .forms import LoginForm



def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)  
        if form.is_valid():                                        
            request.session['login'] = form.user_id                 
            return redirect('/')
    else:
        form = LoginForm()                                         
    
    return render(request, 'login.html', {'form':form})    



def logout(request):
    if request.session['login'] is not None:
        request.session.clear()
        return redirect('/')
    return redirect('/')



def signup(request):
    return render(request, 'signup.html')   

def findId(request):
    return render(request, 'findId.html')   

def findPw(request):
    return render(request, 'findPw.html')   

def signupCheck(request):
    id = request.get['loginId']
    pw = request.get['loginPw']
    
    return redirect('/')


def myOrder(request):
    return render(request, 'myOrder.html')   

def register(request):
    return render(request, 'register.html')   
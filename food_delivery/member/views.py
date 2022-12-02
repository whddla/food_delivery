from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from food_delivery.models import User
from .forms import LoginForm

def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)  
        print('들어옴1')                           
        if form.is_valid():                                        
            request.session['login'] = form.user_no                 
            print('들어옴2')                           
            return redirect('/')
    else:
        print('들어옴3')                           
        form = LoginForm()                                         
    
    print('들어옴4')                           
    return render(request, 'login.html', {'form':form})    




def logout(request):
    if request.session['login'] is not None:
        del request.session['login']
        return redirect('/')
    return render(request, 'login.html')

def signup(request):
    return render(request, "signup.html")
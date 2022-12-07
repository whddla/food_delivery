from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request, "myStore/order.html")

def manage(request):
    return render(request, "myStore/manage.html")

def progress(request):
    return render(request, "myStore/progress.html")

def completion(request):
    return render(request, "myStore/completion.html")
    
def detail(request):
    return render(request, "myStore/detail.html")
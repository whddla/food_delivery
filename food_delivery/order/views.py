from django.shortcuts import render

def order(request):
    return render(request, "user-order.html")
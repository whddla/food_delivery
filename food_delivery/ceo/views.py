from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request, "myStore/order.html")

def manage(request):
    return render(request, "myStore/manage.html")
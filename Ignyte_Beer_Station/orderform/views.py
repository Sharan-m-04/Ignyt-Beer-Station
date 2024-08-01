from django.shortcuts import render

def orderform(request):
    return render(request, 'orderform.html')
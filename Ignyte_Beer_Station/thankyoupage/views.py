from django.shortcuts import render

def thankyou(request):
    return render(request, 'thankyou.html')
from django.shortcuts import render

def gallery(request):
    image_numbers = range(1, 49)
    return render(request, 'gallery.html', {'image_numbers': image_numbers})
from django.shortcuts import render

from .models import CarouselImage

# Create your views here.
def homeView(request):
    template_name = 'mainapp/home.html'
    context = {
        # dictionary with context data.
        'carousel_images' : CarouselImage.objects.all()
        # The above line is equivalent to `SELECT * FROM CarouselImage;`

    }
    return render(request, template_name, context)

def aboutView(request):
    template_name = 'mainapp/about.html'
    context = {
        # dictionary with context data.
    }
    return render(request, template_name, context)

def contactView(request):
    template_name = 'mainapp/contact.html'
    context = {
        # dictionary with context data.
    }
    return render(request, template_name, context)
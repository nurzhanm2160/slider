from django.shortcuts import render
from .models import Image

# Create your views here.


def get_images(request):
    images = Image.objects.all()
    context = {"images": images}

    return render(request, 'index.html', context)

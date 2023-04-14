from django.shortcuts import render
from .models import Image

# Create your views here.


def get_images(request):
    images = Image.objects.all()
    context = {"images": images}
    print(images[1].id)

    return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import random
from .models import Image
from django.core.files.storage import FileSystemStorage


# def index(request):
#     return render(request, 'test.html')

# def imageUpload(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'demo.html', {'form': form})
#     else:
#         form = ImageUploadForm()
#         return render(request, 'demo.html', {'form': form})

# def imageUpload(request):
#     if request.method == 'POST':
#         image_form = Image()
#         image_form.name = request.POST['name']
#         image_form.image = request.FILES['image']
#         fss = FileSystemStorage(location="media/images", base_url="/media/images")
#         files = fss.save(image_form.image, image_form)
#         files_url = fss.url(files)
#         return render(request, 'image.html', {'files_url': files_url})
#     return render(request, 'image.html')

def imageUpload(request):
    if request.method == 'POST':
        image_form = Image()
        image_form.name = request.POST['name']
        image_form.image = request.FILES['image']
        image_form.save()
        return redirect('')
    else:
        return render(request, 'image.html')


def random_test(request):
    test_images_path = './static/images/'
    if request.method == 'POST':
        test_image = random.choice(os.listdir(test_images_path))
        return render(request, 'image.html', {'test_image': test_image})
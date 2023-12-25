from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image
import replicate
import string
import random
from django.core.files.base import ContentFile
from dotenv import load_dotenv
from os import getenv
import requests
load_dotenv()


# ... other imports ...


MODEL_ID = getenv('MODEL_ID')

def filename_gen():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))

def generate_image(text, model=MODEL_ID):
    output = replicate.run(model, input={"prompt": text})
    response = requests.get(output[0])
    if response.status_code == 200:
        # Use ContentFile to create a file-like object from bytes
        image_content = ContentFile(response.content)
        return image_content
    else:
        redirect("write_text")



def write_text(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            # Use generate_image to get the image content
            image_content = generate_image(text)
            
            # Create a new Image instance and set the image field
            new_image = Image(text=text)
            new_image.image.save(f'{filename_gen()}.png', image_content)
            new_image.save()

            return redirect('images')
    else:
        form = ImageForm()
    return render(request, 'write_text.html', {'form': form})

def images(request):
    images = Image.objects.all()
    return render(request, 'images.html', {'images': images})

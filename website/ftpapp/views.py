from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from .forms import ImageUploadForm
from .models import UploadedImage


def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'ftpapp/person_form.html', {'form': form})


def success(request):
    return render(request, 'ftpapp/success.html')


def search_person(request):
    person = None
    query = request.GET.get('id')  
    if query:
        try:
            person = get_object_or_404(Person, id=query)
        except:
            person = None
    return render(request, 'ftpapp/search_person.html', {'person': person})





def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('show_images')  
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload_image.html', {'form': form})

def show_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'show_images.html', {'images': images})




def delete_image(request, image_id):
    image = get_object_or_404(UploadedImage, id=image_id)
    
    image.delete()
    
    return redirect('show_images')  


from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from .forms import ImageUploadForm
from .models import UploadedImage

# Existing view for the form submission
def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'ftpapp/person_form.html', {'form': form})

# Success view
def success(request):
    return render(request, 'ftpapp/success.html')

# New view for search functionality
def search_person(request):
    person = None
    query = request.GET.get('id')  # Get the ID from the search form
    if query:
        try:
            person = get_object_or_404(Person, id=query)
        except:
            person = None
    return render(request, 'ftpapp/search_person.html', {'person': person})

# views.py



def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the image to the database
            return redirect('show_images')  # Redirect to the page that shows all images
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload_image.html', {'form': form})

def show_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'show_images.html', {'images': images})


from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedImage

def delete_image(request, image_id):
    image = get_object_or_404(UploadedImage, id=image_id)
    
    image.delete()
    
    return redirect('show_images')  


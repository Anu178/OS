from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

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

from django import forms
from .models import Person
from .models import UploadedImage

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'mobile_number']
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

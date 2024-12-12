from django.db import models
import uuid
import os

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} {self.surname}"




def image_upload_to(instance, filename):
    # Create a unique folder for each image upload with its ID
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex}.{ext}'  # Generate a unique filename
    return os.path.join('uploads/', filename)  # Save in 'uploads/' directory

class UploadedImage(models.Model):
    image = models.ImageField(upload_to=image_upload_to)  # The uploaded image
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Store when it was uploaded

    def __str__(self):
        return str(self.image)

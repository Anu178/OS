from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.person_form, name='person_form'),
    path('success/', views.success, name='success'),
    path('search/', views.search_person, name='search_person'), 
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.show_images, name='show_images'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
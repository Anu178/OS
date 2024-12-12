from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_form, name='person_form'),
    path('success/', views.success, name='success'),
    path('search/', views.search_person, name='search_person'),  # New URL for search
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('certifications/', views.certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('skills', views.skills, name='skills'),
]

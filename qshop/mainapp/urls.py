# URL routing for mainapp
from django.urls import path
from .views import homeView, aboutView, contactView

urlpatterns = [
    path('', homeView, name='home_page'),
    path('about', aboutView, name='about_page'),
    path('contact', contactView, name='contact_page')
]
# URL routing for mainapp
from django.urls import path

from .views import homeView, aboutView, contactView
from .views import ViewCarouselImages, AddCarouselImage

urlpatterns = [
    path('', homeView, name='home_page'),
    path('carousel/all/', ViewCarouselImages.as_view(), name='carousels_page' ),
    path('carousel/add/', AddCarouselImage.as_view(), name='add_carousel'),


    path('about', aboutView, name='about_page'),
    path('contact', contactView, name='contact_page')
]
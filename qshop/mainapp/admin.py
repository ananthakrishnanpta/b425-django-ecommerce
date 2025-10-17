from django.contrib import admin

# Register your models here.
from .models import CarouselImage



class CustomCarouselManagement(admin.ModelAdmin):
    list_display = ['id', 'title','caption', 'added_at']


admin.site.register(CarouselImage, CustomCarouselManagement)


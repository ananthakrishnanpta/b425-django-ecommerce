from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='products/thumbnails/')
    price = models.PositiveIntegerField()

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.title}"
    
    # This method will be used by CreateView and UpdateView for redirection
    def get_absolute_url(self):
        return reverse("prod_detail", kwargs={"pk": self.pk})

class ProductImage(models.Model):
    caption = models.CharField(max_length=200)
    img = models.ImageField(upload_to='products/images/')
    product = models.ForeignKey(Product, related_name='images', 
                                on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product:{self.product.title} image #{self.id}"
    
    # When success_url is required, after editing and deleting an image, this method
    # will provide url to redirect to the product's detail page
    def get_absolute_url(self):
        return reverse("prod_detail", kwargs={"pk": self.product.pk})
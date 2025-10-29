from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='products/thumbnails/')
    price = models.PositiveIntegerField()

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.title}"

class ProductImage(models.Model):
    caption = models.CharField(max_length=200)
    img = models.ImageField(upload_to='products/images/')
    product = models.ForeignKey(Product, related_name='images', 
                                on_delete=models.CASCADE)
    

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product:{self.product.title} image #{self.id}"
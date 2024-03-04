from django.db import models
from django.urls import reverse

# Create your models here.
# first model based on different categories

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)  # Name of the category can be - shoes, books, etc.

    slug = models.SlugField(max_length=250, unique=True)  # Slug is the unique identifier of the category

    class Meta:
        verbose_name_plural = 'categories'   # This tells django to use this name as for pluralization

    # category 1 , category 2

    def __str__(self):
        return self.name # once object is created it will reaturn its name

    def get_absolute_url(self):
        return reverse('list_category', args=[self.slug])
    
class Product(models.Model):

    # Foreign key to add all in the category. If any category is delete then other categories are casacaded.
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default="Un-Branded")

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='images/')
    
    class Meta:

        verbose_name_plural = 'products'

    # product(1) product(2) product(3)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
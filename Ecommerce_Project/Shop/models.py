from django.db import models
from django.urls import reverse

# Create your models here.
class Category (models.Model):
    Name = models.CharField(max_length=250,unique=True)
    Slug = models.SlugField(max_length=250, unique=True)
    Description = models.TextField(blank=True)
    Image = models.ImageField(upload_to='Category',blank=True)

    class Meta:
        ordering=('Name',)
        verbose_name='Category'
        verbose_name_plural='Categories'

    def get_url(self):
        return reverse('Shop:Products_By_Category',args=[self.Slug])

    def __str__(self):
        return '{}'.format(self.Name)

class Product (models.Model):
    Name = models.CharField(max_length=250, unique=True)
    Slug = models.SlugField(max_length=250, unique=True)
    Description = models.TextField(blank=True)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Product',blank=True)
    Stock = models.IntegerField()
    Available = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('Shop:Products_Category_Detail',args=[self.Category.Slug,self.Slug])

    class Meta:
        ordering=('Name',)
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return '{}'.format(self.Name)
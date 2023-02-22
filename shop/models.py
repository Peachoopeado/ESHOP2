from django.db import models
from django.urls import reverse

# Create your models here.

class VehicleType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class OilType(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Viscosity(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Compound(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Fuel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Transmission(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    vehicle_type = models.ManyToManyField(VehicleType, blank=True)
    oiltype = models.ManyToManyField(OilType, blank = True)
    transmission = models.ManyToManyField(Transmission, blank=True)
    viscosity = models.ManyToManyField(Viscosity, blank = True)
    compound = models.ManyToManyField(Compound, blank = True)
    fuel = models.ManyToManyField(Fuel, blank=True)


    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product-list', args=[self.slug])
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='shop/img/products')
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, blank=True, default=True)
    oiltype = models.ForeignKey(OilType, on_delete=models.CASCADE)
    viscosity = models.ForeignKey(Viscosity, on_delete=models.CASCADE)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product-detail', args=[self.id])
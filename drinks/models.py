from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table ='menus'
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta: 
        db_table ='categories'

class Product(models.Model):
    
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    english_name = models.CharField(max_length=100)
    korean_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    nutrition = models.ForeignKey('Nutrition',on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'products'


class Images(models.Model):
    image_url = models.URLField()
    product = models.ForeignKey('Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml = models.CharField(max_length=100)
    size_fluid_ounce = models.CharField(max_length=100)

    class Meta:
        db_table = 'nutritions'

    
class Allergy(models.Model):
    
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'allergies'

class Allergy_products(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergies_products'
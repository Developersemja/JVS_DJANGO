from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.core.exceptions import ValidationError



class Category(models.Model):
    cid = ShortUUIDField(length=6, max_length=30, prefix="CAT-", alphabet="0123456789", default="")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    pid = ShortUUIDField(length=6, max_length=30, prefix="PRD-", alphabet="0123456789", default="")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    featured_product = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    feature = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Product_image/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="Product_images/",default="prd.jpg")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="p_images")

 
class Offer(models.Model):
    image = models.ImageField(upload_to='Gif_offer/')
    big_image = models.ImageField(upload_to='big_offer_image/')
    marquee=models.CharField(max_length=100)

    def __str__(self):
        return self.marquee

class OfferImages(models.Model):
    images = models.ImageField(upload_to="offer_multi_images/",default="offer.jpg",)
    Offer = models.ForeignKey(Offer,on_delete=models.SET_NULL,null=True,related_name="offer_images")

    
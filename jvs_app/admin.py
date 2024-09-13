from django.contrib import admin
from .models import Product, Category , Offer , OfferImages , ProductImages 
from django.core.exceptions import ValidationError

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['name','price','featured_product','date','pid','category']


class OfferImagesAdmin(admin.TabularInline):
    model= OfferImages

class OfferAdmin (admin.ModelAdmin):
    inlines = [ OfferImagesAdmin]


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Offer,OfferAdmin)

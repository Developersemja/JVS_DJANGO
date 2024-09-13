from django.shortcuts import render
from jvs_app.models import Category,Product,Offer

def index(request):
    Products=Product.objects.all()
    Categories= Category .objects.all()
    offers=Offer.objects.all()
    featured_products = Product.objects.filter(featured_product=True)
    offer_images = []
    for offer in offers:
        offer_images.extend(offer.offer_images.all()) 
    context={
        'products':Products,
        'category':Categories,
        'offer': offers,
        'featured_product':featured_products,
        'offer_multi':offer_images,
    }
    return render(request, 'index.html',context)


def category(request):
    Categories= Category .objects.all()
    offers=Offer.objects.all()
    context={
        'category':Categories, 'offer': offers,
    }
    return render(request, 'category.html',context)


def category_list(request,cid):
    category = Category.objects.get(cid=cid)
    products= Product.objects.filter(category=category)
    context={
        "Category":category,"product":products,
    }
    return render(request,"category_list.html",context)


def contact(request):
    return render(request, 'contact.html')


def products(request):
    Products=Product.objects.all()
    offers=Offer.objects.all()
    context={
        'products':Products, 'offer': offers,
    }
    return render(request, 'products.html',context)
 
 
def product_details(request,pid):
    Products=Product.objects.get(pid=pid)
    features = Products.feature.split(',')
    p_image = Products.p_images.all()

    context={
        'p':Products, 'p_images':p_image,'feature':features,
    }
    print(context)
    return render(request, 'product_detail_page.html',context)   
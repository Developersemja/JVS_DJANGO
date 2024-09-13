from django.urls import path
from jvs_app.views import index,category,contact,products,product_details,category_list


urlpatterns = [
    path('', index, name='index'),  

    path('category/', category, name='category'),  
    path('category/<cid>', category_list, name='category_list'),  

    path('contact/', contact, name='contact'),  

    path('products/', products, name='products'),  
    path('product_details/<pid>', product_details, name='product_details'),  
]
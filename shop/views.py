from django.shortcuts import render,get_object_or_404
from .models import Book,Category
from cart.forms import CartAddProductForm
# Create your views here.

def indexView(request,categoryid = None):
    category = None
    categories = Category.objects.all()
    booklist = Book.objects.filter(sale=True)
    if categoryid:
        category = get_object_or_404(Category,id=categoryid)
        booklist = booklist.filter(category=category)
    return render(request,'shop/index.html',{'booklist':booklist,
                                             'category':category,
                                             'categories':categories})

def book_detail(request,id):
    book = get_object_or_404(Book,id=id,sale=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/detail.html',{'book':book,
                                              'cart_product_form':cart_product_form})

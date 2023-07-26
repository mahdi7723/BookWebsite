from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Book, Category, Author, CartItem
from django.contrib.auth.decorators import login_required


def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    book_paginator = Paginator(books, 6)
    book_page_number = request.GET.get('book_page')
    book_page_obj = book_paginator.get_page(book_page_number)

    author_paginator = Paginator(authors, 5)
    author_page_number = request.GET.get('author_page')
    author_page_obj = author_paginator.get_page(author_page_number)

    return render(request, 'home.html', {'book_page_obj': book_page_obj, 'author_page_obj': author_page_obj})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    author = book.author
    author_books = Book.objects.filter(author=author)

    context = {
        'book': book,
        'author': author,
        'author_books': author_books,
    }
    return render(request, 'book_detail.html', context)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'book/category_list.html', {'categories': categories})


def author_book(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    author_books = Book.objects.filter(author=author)

    context = {
        'author': author,
        'author_books': author_books,
    }

    return render(request, 'author_book.html', context)


@login_required
def add_to_cart(request, book_id):
    product = Book.objects.get(pk=book_id)
    user = request.user

    # Check if the item already exists in the cart, if yes, update the quantity, else create a new entry.
    try:
        cart_item = CartItem.objects.get(product=product, user=user)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem(product=product, user=user)
        cart_item.save()

    return redirect('cart')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')


@login_required
def cart_view(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)


@login_required
def increase_quantity(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

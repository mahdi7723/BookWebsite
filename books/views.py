from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Book, Category, Author


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

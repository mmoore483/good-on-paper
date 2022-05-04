from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q


def all_books(request):
    """ a view to show all books, including sorting and search queries """
    books = Book.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('books'))
            queries = Q(author__icontains=query) | Q(description__icontains=query) | Q(
                genres__icontains=query) | Q(isbn__icontains=query) | Q(series__icontains=query)
            books = books.filter(queries)
    context = {
        "books": books,
        "search_term": query,
    }

    return render(request, 'books/book.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)

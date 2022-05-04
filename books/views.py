from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q


def all_books(request):
    """ a view to show all books, including sorting and search queries """
    books = Book.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'price':
                sortkey = 'price'
            if sortkey == 'rating':
                sortkey = 'rating'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

        if 'genres' in request.GET:
            genresq = request.GET['genres']
            books = books.filter(Q(genres__icontains=genresq))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('books'))
            queries = Q(author__icontains=query) | Q(description__icontains=query) | Q(
                genres__icontains=query) | Q(isbn__icontains=query) | Q(series__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        "books": books,
        "search_term": query,
        "current_sorting": current_sorting,
    }

    return render(request, 'books/book.html', context)


def book_detail(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)

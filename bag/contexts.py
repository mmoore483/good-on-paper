from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def bag_contents(request):

    bag_items = []
    total = 0
    book_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        book = get_object_or_404(Book, pk=item_id)
        total += item_data * book.price
        book_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'book': book,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'book_count': book_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

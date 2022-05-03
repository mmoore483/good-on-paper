from django.contrib import admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "book_id",
	    "title",
	    "author",
	    "price",
	)
    ordering = ("book_id",)

admin.site.register(Book, BookAdmin)
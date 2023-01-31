from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    """
    The list_display variable in this BookAdmin class is used to specify the number of columns in the
    Admin interface that are seen for the contents of the model. It can also make use of functions and methods.

    The list_filter variable in this BookAdmin class is used to filter books by the publisher

    The date_hierarchy variable allows us to navigate books by the year.

    The search_fields variable allows us to place a search bar.
    """
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    date_hierarchy = 'publication_date'
    search_fields = ('title', 'isbn', 'publisher_name')
    def isbn13(self, obj):
        """
        '9780316769174' => '978-0-31-676917-4'
        """
        return f"{obj.isbn[0:3]}-{obj.isbn[3:4]}-{obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}"

class ContributorAdmin(admin.ModelAdmin):
    list_display  = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',) # Excludes the date edited field in the review form

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)


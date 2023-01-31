from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

def initialed_name(obj):
    """
    obj.first_names = 'Jerome David'
    obj.last_names  = 'Salinger'

    'Salinger, JD'
    """
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return f"{obj.last_names}, {initials}"

class BookAdmin(admin.ModelAdmin):
    """
    The list_display variable in this BookAdmin class is used to specify the number of columns in the
    Admin interface that are seen for the contents of the model. It can also make use of functions and methods.
    """
    list_display = ('title', 'isbn13')
    def isbn13(self, obj):
        """
        '9780316769174' => '978-0-31-676917-4'
        """
        return f"{obj.isbn[0:3]}-{obj.isbn[3:4]}-{obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}"

class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialed_name,)

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)


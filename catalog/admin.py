from django.contrib import admin

# imports the models
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# calls admin.site.register to register each model.


class BooksInline(admin.TabularInline):
    model = Book
    exclude = ['summary']
    extra = 0

#admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    #pass # leaves unchanged from admin.site.register(Author)
    # use list_display to add additional fields to the view
    # field names to be displayed in the list are declared in a tuple in the required order
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # The fields attribute lists just those fields that are to be displayed on the form, in order.
    # Fields are displayed vertically by default, but will display horizontally if you further
    # group them in a tuple (as shown in the "date" fields above).
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# declaring inlines, of type TabularInline (horizontal layout) or StackedInline (vertical layout,
# just like the default model layout).
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


#admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #pass

    # Getting the genre may not be a good idea here, because of the "cost" of the database operation.
    # We're showing you how because calling functions in your models can be very useful for
    # other reasons — for example to add a Delete link next to every item in the list.
    list_display = ('title', 'author', 'display_genre')

    # inline for book instance
    inlines = [BooksInstanceInline]


#admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #pass
    #list_display = ('book', 'status', 'due_back','id')

    # It can be useful to be able to filter which items are displayed.
    # This is done by listing fields in the list_filter attribute
    list_filter = ('status', 'due_back')

    # You can add "sections" to group related model information within the detail form,
    # using the fieldsets attribute.7
    # Each section has its own title (or None, if you don't want a title)
    # and an associated tuple of fields in a dictionary
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)
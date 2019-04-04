from django.contrib import admin
from accounts.models import Publisher, Book, Author

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)

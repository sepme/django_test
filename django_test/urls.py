from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts.views import BookList, AuthorList, PublisherList, add_book, add_author, add_publisher

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('book-list/', BookList.as_view(), name='book_list'),
    path('author-list/', AuthorList.as_view(), name='author_list'),
    path('publisher-list/', PublisherList.as_view(), name='publisher_list'),
    path('add-book/', add_book, name='book_add'),
    path('add-author/', add_author, name='author_add'),
    path('add-publisher/', add_publisher, name='publisher_add'),
    path('admin/', admin.site.urls),
    path('catalog/', TemplateView.as_view(template_name='home.html'), name='home')
]

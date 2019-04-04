from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts.views import BookList, add_book

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('book-list', BookList.as_view(), name='book_list'),
    path('add-book/', add_book, name='book_add'),
    path('admin/', admin.site.urls),
    path('catalog/', TemplateView.as_view(template_name='home.html'), name='home')
]

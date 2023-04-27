
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.Test.as_view(), name='index'),
    path('booklist', views.BookListView.as_view(), name='index'),
    path('book/<pk>', views.BookDetailView.as_view(), name='index'),
    path('createbook', views.CreateBookView, name='index'),
]
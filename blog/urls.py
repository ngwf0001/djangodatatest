
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.Home.as_view(), name='home'),
    path('test', views.Test.as_view(), name='index'),
    path('booklist', views.BookListView.as_view(), name='booklist'),
    path('booklist2', views.BookListView2.as_view(), name='booklist2'),
    path('book/<pk>', views.BookDetailView.as_view(), name='bookdetail'),
    path('update/<pk>', views.BookUpdateView.as_view(), name='bookupdate'),
    path('createbook', views.BookCreateView.as_view(), name='index'),
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('upload', views.upload_file, name='upload'),
    path('update2/<pk>', views.bookupdate, name='bookupdate2'),
    path('testsession', views.testsession, name='testsession'),
    path('testsession2', views.testsession, name='testsession2'),
    path('testfilters', views.testfilters, name='testfilters'),
] 
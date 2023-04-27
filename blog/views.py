from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *
from .forms import BookForm

# Create your views here.
def index(request):
    return HttpResponse('hello world')

class Home(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return HttpResponse('hello world')
        
    def post(self, request: HttpRequest):
        pass
    



class Test(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return HttpResponse('hello world, this is a test')
        
    def post(self, request: HttpRequest):
        return HttpResponse('direct to post')

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    queryset = Book.objects.filter(title__icontains='China')
    

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = 'book'

    
def CreateBookView(request: HttpRequest):
    form = BookForm(request.POST)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    return render(request, 'book_form.html', {'form': form})
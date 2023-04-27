from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import BookForm

# Create your views here.
def index(request):
    return HttpResponse('hello world')

class Home(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return HttpResponse('hello world')
        
    def post(self, request: HttpRequest):
        return HttpResponse('direct to post')
    



class Test(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = BookForm()
        return render(request, 'book_form.html', {'form': form})
        
    def post(self, request: HttpRequest):
        response = HttpResponse('success<br/>')
        response.write('how are you?<br/>')
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            book = form.save(commit=False)
            title = form.cleaned_data['title']
            description=form.cleaned_data['desc']
            author = form.cleaned_data['author']
            book.title = title + ' --- a good title'
            book.desc = description + ' --- a good book'
            book.save()
            print(book)
            
            
        return response

class BookListView2(ListView):
    model = Book
    template_name = 'book_list.html' #default is 'book_list.html'
    context_object_name = 'books' #default is 'objects'
    queryset = Book.objects.filter(title__icontains='China')
    
    


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html' #default is 'book_list.html'
    context_object_name = 'books' #default is 'objects'
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs) #qs = super(BookListView,self).get_queryset(*args, **kwargs)
        qs = qs.order_by('-title')
        return qs
    
    # queryset = Book.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['love'] = 'I love you'
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = 'book'

    
def createBookView(request: HttpRequest):
    form = BookForm(request.POST)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    return render(request, 'book_form.html', {'form': form})

class BookCreateView(CreateView):
    model = Book
    template_name = "Book_create.html"
    context_object_name = 'book'
    fields = ['title', 'desc', 'author']
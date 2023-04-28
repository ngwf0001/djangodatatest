from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *
from .forms import BookForm, UploadFileForm, BookUpdateForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 

def handle_uploaded_file(f):
    with open("abc.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
# @login_required
def index(request):
    return HttpResponse('hello world')

def upload_file(request):
    if request.method == "POST":
        print(request.POST)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            # return HttpResponseRedirect("/success/url/") 
            return HttpResponse('Successfully uploaded file')

    
    form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


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
    
    


class BookListView(LoginRequiredMixin, ListView):
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
        context['love'] = f"I love you {self.request.session['username']}"
        return context

@method_decorator(login_required, name='dispatch')
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
    
class MyLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        self.request.session['username'] = self.request.POST['username']
        return reverse_lazy('booklist')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid user name or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class BookUpdateView(UpdateView):
    # specify the model you want to use
    model = Book
    template_name = "book_update.html"
    context_object_name = 'book'
    fields = ['title', 'desc', 'author']
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        book = form.save(commit=False)
        book.title = self.request.POST['title'] + ' --- a good title'
        book.save()
        # form.save_m2m()
        return super().form_valid(form)
    
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"
    
def bookupdate(request, pk):
    # dictionary for initial data with
    # field names as keys
        context ={}
    
        # fetch the object related to passed id
        obj = get_object_or_404(Book, id = pk)
    
        # pass the object as instance in form
        form = BookUpdateForm(request.POST or None, instance = obj)
    
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+pk)

    
        # add form dictionary to context
        context["form"] = form
    
        return render(request, "book_update.html", context)
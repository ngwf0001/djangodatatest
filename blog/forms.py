from django.forms import ModelForm
from .models import Book
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'author']
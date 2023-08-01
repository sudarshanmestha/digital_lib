from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request, 'digital_lib_app/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            new_book = upload.save()
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("Somthing went wrong. please reload the webpage by clicking <a href='{}'>here</a>".format(reverse('index')))    

    else:
        return render(request, 'digital_lib_app/upload.html', {'upload_form': upload})


def update_book(request, book_id):
    book_id = int(book_id)
    book_shelf = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book_form = BookCreate(request.POST, request.FILES, instance=book_shelf)
        if book_form.is_valid():
            book_form.save()
            return redirect('index')
    else:
        book_form = BookCreate(instance=book_shelf)

    return render(request, 'digital_lib_app/upload.html', {'upload_form': book_form})         

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_shelf.delete()
    return redirect('index')    

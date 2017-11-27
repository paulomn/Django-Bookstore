from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models.app.book import Book

def books(request):
    assert isinstance(request, HttpRequest)
    
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect('/')
    else:
        all_books = Book.objects.all()
        return render(
            request,
            'app/books.html',
            {
                'title':'Books Management',
                'message': 'Add or view the books collection',
                'all_books': all_books,
            }
        )
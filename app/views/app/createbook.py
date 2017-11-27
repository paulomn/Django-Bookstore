from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from datetime import datetime
from app.forms import CreateBookForm

def createbook(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBookForm()
        return render(request, 'app/createbook.html', {'form': form})
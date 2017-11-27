from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from datetime import datetime

def detail(request, id):
    assert isinstance(request, HttpRequest)
    
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('<h3>User identification: ' + str(id) + '</h3>')

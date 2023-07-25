from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>string as a response in app3</h1>')

def second(request):
    return HttpResponse('<h1> second string as a response in app3</h1>')

def app3_first(request):
    return render(request,'app3_first.html')
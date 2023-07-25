from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return render(request,'first.html')

def second(request):
    return render(request,'second.html')

def first1(request):
    return HttpResponse('<h1>string as a response in app1</h1>')
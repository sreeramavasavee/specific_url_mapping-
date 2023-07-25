from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return render(request,'app2_first.html')

def app2_second(request):
    return render(request,'app2_second.html')

def first1(request):
    return HttpResponse('<h1>string as a response in app2</h1>')
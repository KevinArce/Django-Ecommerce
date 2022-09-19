from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> HttpRequest
# request handler for the home page

def calculate():
    y = 2
    return 1

def say_hello(request):
    x = calculate()

    return render(request, 'hello.html', {'name': 'Kevin'})
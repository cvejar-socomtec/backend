from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Index app2</h1>")

def texto(request):
    return HttpResponse("<p>soy un parrafo de app2</p>")
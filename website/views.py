from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Page from the theme 
    return render(request, 'pages/home.html')
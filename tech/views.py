from django.shortcuts import render

# Create your views here.

def tech_home(request):
    return render(request, 'index.html')
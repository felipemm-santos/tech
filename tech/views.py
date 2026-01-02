from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def tech_home(request):
    return render(request, 'index.html')

@login_required
def members_area(request):
    return render(request, 'members.html')
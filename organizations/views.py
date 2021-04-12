from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,'organizations/home.html')

@login_required
def create(request):
    return render(request, 'organizations/create.html')
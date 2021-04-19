from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NgoForm
from django.views.generic.edit import CreateView
from .models import Ngos

# Create your views here.

class NgoCreateView(CreateView):
    model = Ngos
    fields = '__all__'

def home(request):
    return render(request,'ngos/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = NgoForm(request.POST)
        if form.is_valid():
            choices = form.cleaned_data.get('choices')
            # do something with your results
    else:
        form = NgoForm

    return render(request, 'ngos/create.html',{'form':form})


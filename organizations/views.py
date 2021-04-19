from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OrganizationForm
from django.views.generic.edit import CreateView
from .models import Organization


#Create your views here.

class OrganizationCreateView(CreateView):
    model = Organization
    fields = '__all__'

def home(request):
    return render(request,'organizations/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            choices = form.cleaned_data.get('choices')
            # do something with your results
    else:
        form = OrganizationForm

    return render(request, 'organizations/create.html')

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NgoForm
from django.views.generic.edit import CreateView
from .models import Ngos
from django.conf import settings

# Create your views here.

class NgoCreateView(CreateView):
    model = Ngos
    fields = '__all__'

def home(request):
    ngos = Ngos.objects.all()
    return render(request,'ngos/home.html', {'ngos':ngos, 'media_url':settings.MEDIA_URL})


def children(request):
    ngos = Ngos.objects.all().filter(children=True)
    return render(request,'ngos/children.html', {'ngos':ngos, 'media_url':settings.MEDIA_URL})

def women(request):
    ngos = Ngos.objects.all().filter(women=True)
    return render(request,'ngos/women.html', {'ngos':ngos})

def elderly(request):
    ngos = Ngos.objects.all().filter(elderly=True)
    return render(request,'ngos/elderly.html', {'ngos':ngos})

def cancer(request):
    ngos = Ngos.objects.all().filter(cancer=True)
    return render(request,'ngos/cancer.html', {'ngos':ngos, 'media_url':settings.MEDIA_URL})

def homeless(request):
    ngos = Ngos.objects.all().filter(homeless=True)
    return render(request,'ngos/homeless.html', {'ngos':ngos})

def hunger(request):
    ngos = Ngos.objects.all().filter(hunger=True)
    return render(request,'ngos/hunger.html', {'ngos':ngos})

def differently_abled(request):
    ngos = Ngos.objects.all().filter(differently_abled=True)
    return render(request,'ngos/differently_abled.html', {'ngos':ngos})


@login_required
def create(request):
    if request.method == 'POST':
        form = NgoForm(request.POST,request.FILES)
        ngo = Ngos()
        if form.is_valid():
            choices = form.cleaned_data
            ngo.title = choices['title']
            ngo.description = choices['description']
            ngo.email = choices['email']
            ngo.registration_number = choices['registration_number']
            ngo.contact = choices['contact']
            ngo.url = choices['url']
            ngo.image = choices['image']
            ngo.thumbnail = choices['thumbnail']
            ngo.hunger = choices['hunger']
            ngo.homeless = choices['homeless']
            ngo.women = choices['women']
            ngo.children = choices['children']
            ngo.elderly = choices['elderly']
            ngo.cancer = choices['cancer']
            ngo.differently_abled = choices['differently_abled']
            ngo.account = request.user
            ngo.save()
            return redirect('/ngos/' + ngo.registration_number)
    else:
        form = NgoForm

    return render(request, 'ngos/create.html',{'form':form})


def detail(request, registration_number):
    ngo = get_object_or_404(Ngos, pk=registration_number)
    return render(request, 'ngos/detail.html',{'ngo':ngo,'media_url':settings.MEDIA_URL})

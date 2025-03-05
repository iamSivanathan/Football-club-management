from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse
from .models import Players,TeamStanding
from .forms import PlayerForm, TeamStandingForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def team(request):
    return render(request,'team.html')

# standing
def standing(request):
    ts = TeamStanding.objects.all().order_by('-points')
    return render(request, 'standing.html', {'ts': ts})

def standadd(request):
    sform = TeamStandingForm()

    if request.method == 'POST':
        sform = TeamStandingForm(request.POST)
        if sform.is_valid():
            sform.save()
            return redirect('standing')        
    return render(request,'standadd.html',{'sform':sform})



def standform(request, pk):
    team = TeamStanding.objects.get(id=pk)
    sform = TeamStandingForm(instance=team)
    if request.method == "POST":
        sform = TeamStandingForm(request.POST, instance=team)
        if sform.is_valid():
            sform.save()
            return redirect('standing')
        return render(request,'standform.html',{'sform':sform})
    
    else:
        sform = TeamStandingForm(instance=team)  
    return render(request, 'standform.html', {'sform': sform})


# players

def player(request):
    pl=Players.objects.all()
    return render(request,'player.html',{'pl':pl})

def add(request):
    pform = PlayerForm()

    if request.method == 'POST':
        pform = PlayerForm(request.POST)
        if pform.is_valid():
            pform.save()
            return redirect('player')        
    return render(request,'add.html',{'pform':pform})

def update(request,pk):
    upd= Players.objects.get(id=pk)
    pform = PlayerForm(instance=upd)
    if request.method == 'POST':
        pform = PlayerForm(request.POST,instance=upd)    
        if pform.is_valid():
            pform.save()
            return redirect('player')
    return render(request,'update.html',{"pform":pform})    

def remove(request,pk):
    upd = Players.objects.get(id=pk)
    if request.method == 'POST':
        upd.delete()
        return redirect('player')
    return render(request,'remove.html',{'upd':upd})



def contact(request):
    return render(request,'contact.html')
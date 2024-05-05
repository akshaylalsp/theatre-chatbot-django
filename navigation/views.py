from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def theatre(request):
    return render(request,'theatre.html')

@login_required
def location(request):
    pass

@login_required
def askme(request):
    return redirect('http://localhost:8501/')

@login_required
def showtime(request):
    return render(request,'home.html')
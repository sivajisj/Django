from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginUserForm, AddRecordForm, UpdateRecordForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Record
# Create your views here.

def home(request):
    return render(request,"webapp/index.html")

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
            
    context = {'form': form}
    return render(request, 'webapp/register.html', context)

def login_view(request):
    form = LoginUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")       
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context)
            
# Dashboard
@login_required(login_url='login') 
def dashboard(request):
    my_record = Record.objects.all()
    context = {'records' : my_record}
    return render(request, 'webapp/dashboard.html',context)


def user_logout(request):
    if request.user.is_authenticated :
        logout(request)
    return redirect("home-page")

@login_required(login_url='login')
def create_record(request):
    form = AddRecordForm()
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)

@login_required(login_url='login')
def update_record(request):
    
    pass
    

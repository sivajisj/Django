from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserCreationForm, LoginUserForm, AddRecordForm, UpdateRecordForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"webapp/index.html")

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
        
            
    context = {'form': form}
    return render(request, 'webapp/register.html', context)


    
def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, " login successful")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = LoginUserForm()

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
        messages.success(request, "logged out")
    return redirect("home-page")

@login_required(login_url='login')
def create_record(request):
    form = AddRecordForm()
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "new record created successfully")
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)

@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record was successfully updated")
            return redirect("dashboard")
    else:
        form = UpdateRecordForm(instance=record)
        context = {'form': form}
    return render(request, 'webapp/update-record.html',context)
    
@login_required(login_url='login')    
def view_record(request,pk):
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request, 'webapp/view-record.html',context)

@login_required(login_url="login")
def delete_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "record was deleted successfully")
        return redirect('dashboard')
    context = {'record': record}
    return render(request, 'webapp/delete-record.html', context)
    


from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginUserForm
# Create your views here.

def home(request):
    return render(request,"webapp/index.html")

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'webapp/register.html', context)
            



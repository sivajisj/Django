from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = "ben"
    context = {"name": name}
    return render(request, 'index.html',context=context)

def counter(request):
    text = request.GET.get('text', '')
    context = {"text": text}
    return render(request, 'counter.html', context=context)
    # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    # .\.env1\Scripts\Activate.ps1
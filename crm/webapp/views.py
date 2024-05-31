from django.shortcuts import render

# Create your views here.
def register_view(request):
    pass


def home(request):
    return render(request,"webapp/base.html")

from django.shortcuts import render

def printFirstApp(request):
    return render(request, 'index.html')
# Create your views here.

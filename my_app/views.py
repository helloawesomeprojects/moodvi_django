from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name='Adam'
    return render(request, 'index.html',{'name':name})
def cout(request):
    return render(request,'count.html')

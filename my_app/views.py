from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name='Adam'
    return render(request, 'index.html',{'name':name})
def count(request):
    words=request.POST['text']
    amount=len(words.split())
    return render(request,'count.html',{'amount':amount})

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tasks = ["watch", "walk", "read", "sleep"]

def test(request):
    return render(request,"tasks.html",{
        "tasks":tasks
    
    })
def add(request):
    return render(request,"add.html")

from django.shortcuts import render

from django import forms

from django.http import HttpResponse
# Create your views here.
tasks = ["watch", "walk", "read", "sleep"]
class NewTaskforms(forms.Form):
    task = forms.CharField(label="Tasks")
    #phone = forms.IntegerField(label="Phone Number", min_value="10",max_value="12")


def test(request):
    return render(request,"tasks.html",{
        "tasks":tasks
    
    })
def add(request):
    if request.method == "POST":
        form = NewTaskforms(request.POST)
        if form.is_valid():
            task =form.cleaned_data["task"]
            tasks.append(task)
        else:
             return render(request,"add.html",{
            "form":form
        })

    return render(request,"add.html",{
        "form":NewTaskforms()
    })
def ongeza(request):
    return render(request, "ongeza.html",{
        "email":NewTaskforms
    })




